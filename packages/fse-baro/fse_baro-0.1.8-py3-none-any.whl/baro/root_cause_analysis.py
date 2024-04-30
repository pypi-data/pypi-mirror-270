import pandas as pd
from sklearn.preprocessing import RobustScaler, StandardScaler

from .utility import drop_time, drop_constant, drop_near_constant


def select_useful_cols(data):
    selected_cols = []
    for c in data.columns:
        # keep time
        if "time" in c:
            selected_cols.append(c)

        # cpu
        if c.endswith("_cpu") and data[c].std() > 1:
            selected_cols.append(c)

        # mem
        if c.endswith("_mem") and data[c].std() > 1:
            selected_cols.append(c)

        # latency
        # if ("lat50" in c or "latency" in c) and (data[c] * 1000).std() > 10:
        if "lat50" in c and (data[c] * 1000).std() > 10:
            selected_cols.append(c)
    return selected_cols



def drop_extra(df: pd.DataFrame):
    if "time.1" in df:
        df = df.drop(columns=["time.1"])

    # remove cols has "frontend-external" in name
    # remove cols start with "main_" or "PassthroughCluster_", etc.
    for col in df.columns:
        if (
            "frontend-external" in col
            or col.startswith("main_")
            or col.startswith("PassthroughCluster_")
            or col.startswith("redis_")
            or col.startswith("rabbitmq")
            or col.startswith("queue")
            or col.startswith("session")
            or col.startswith("istio-proxy")
        ):
            df = df.drop(columns=[col])

    return df




def convert_mem_mb(df: pd.DataFrame):
    # Convert memory to MBs
    def update_mem(x):
        if not x.name.endswith("_mem"):
            return x
        x /= 1e6
        # x = x.astype(int)
        return x

    return df.apply(update_mem)


def preprocess(data, dataset=None, dk_select_useful=False):
    data = drop_constant(drop_time(data))
    data = convert_mem_mb(data)

    if dk_select_useful is True:
        data = drop_extra(data)
        data = drop_near_constant(data)
        data = data[select_useful_cols(data)]
    return data





def nsigma(data, inject_time=None, dataset=None, num_loop=None, sli=None, anomalies=None, **kwargs):
    if anomalies is None:
        normal_df = data[data["time"] < inject_time]
        anomal_df = data[data["time"] >= inject_time]
    else:
        normal_df = data.head(anomalies[0])
        # anomal_df is the rest
        anomal_df = data.tail(len(data) - anomalies[0])

    normal_df = preprocess(
        data=normal_df, dataset=dataset, dk_select_useful=kwargs.get("dk_select_useful", False)
    )

    anomal_df = preprocess(
        data=anomal_df, dataset=dataset, dk_select_useful=kwargs.get("dk_select_useful", False)
    )

    # intersect
    intersects = [x for x in normal_df.columns if x in anomal_df.columns]
    normal_df = normal_df[intersects]
    anomal_df = anomal_df[intersects]

    ranks = []

    for col in normal_df.columns:
        a = normal_df[col].to_numpy()
        b = anomal_df[col].to_numpy()

        scaler = StandardScaler().fit(a.reshape(-1, 1))
        zscores = scaler.transform(b.reshape(-1, 1))[:, 0]
        score = max(zscores)
        ranks.append((col, score))

    ranks = sorted(ranks, key=lambda x: x[1], reverse=True)
    ranks = [x[0] for x in ranks]

    return {
        "node_names": normal_df.columns.to_list(),
        "ranks": ranks,
    }


def robust_scorer(
    data, inject_time=None, dataset=None, num_loop=None, sli=None, anomalies=None, **kwargs
):
    if anomalies is None:
        normal_df = data[data["time"] < inject_time]
        anomal_df = data[data["time"] >= inject_time]
    else:
        normal_df = data.head(anomalies[0])
        # anomal_df is the rest
        anomal_df = data.tail(len(data) - anomalies[0])

    normal_df = preprocess(
        data=normal_df, dataset=dataset, dk_select_useful=kwargs.get("dk_select_useful", False)
    )

    anomal_df = preprocess(
        data=anomal_df, dataset=dataset, dk_select_useful=kwargs.get("dk_select_useful", False)
    )

    # intersect
    intersects = [x for x in normal_df.columns if x in anomal_df.columns]
    normal_df = normal_df[intersects]
    anomal_df = anomal_df[intersects]

    ranks = []

    for col in normal_df.columns:
        a = normal_df[col].to_numpy()
        b = anomal_df[col].to_numpy()

        scaler = RobustScaler().fit(a.reshape(-1, 1))
        zscores = scaler.transform(b.reshape(-1, 1))[:, 0]
        score = max(zscores)
        ranks.append((col, score))

    ranks = sorted(ranks, key=lambda x: x[1], reverse=True)
    ranks = [x[0] for x in ranks]

    return {
        "node_names": normal_df.columns.to_list(),
        "ranks": ranks,
    }


