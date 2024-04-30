
def Echo(_Client:str, _Message:str):
    QueryList:list = []
    QueryList.append({
        "Debug/Echo": {
            "Message": _Message
        }
    })
    Response = _Client.RequestHandler.BuildPostQuery(QueryList, "/EVM")[0]

    return Response
