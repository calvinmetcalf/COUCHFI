import csv,json,couchdbkit

def n(l):
    d=csv.DictReader(open(l))
    i=55245
    r=p(d.next())
    l=r
    r=p(d.next())
    i=i-2
    out=[]
    while r:
        if l["p"]==r["p"]:
            l["n"].append(r["n"][0])
        else:
            out.append({"point":l["p"],"networks":l["n"]})
            l=r
        try:
            r=p(d.next())
        except:
            r=0
    out.append({"point":l["p"],"networks":l["n"]})     
    return out

def p(obj):
    point={"loc":{"lat":obj["CurrentLatitude"],"lng":obj["CurrentLongitude"]},"alt":obj["AltitudeMeters"],"acc":obj["AccuracyMeters"]}
    net={"SSID":obj["SSID"],"MAC":obj["MAC"],"fs":obj["FirstSeen"],"Kind":obj["Type"],"ch":obj["Channel"],"modes":obj["AuthMode"],"strength":obj["RSSI"]}
    return {"p":point,"n":[net]}

def js(o,l):
    j=open(o,"w")
    ll=n(l)
    json.dump(ll,j,ensure_ascii=False)
    j.close()

def up(u,l):
	server = couchdbkit.Server(u)
	db = server.get_or_create_db("w")
	docs= n(l)
 	db.bulk_save(docs)



