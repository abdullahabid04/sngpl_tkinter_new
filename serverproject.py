@app.route('/v/aja/sngpl_hard/<token>&tbs=<tbsn>&press=<pres>', methods=['GET', 'POST'])
def hardware_sngpl(token, tbsn, pres):
    if str(token) in "ajkER8ERNFNJmxngnxcgiuNSJFDGGORTFEser888er":
        value = "1"
        searchdb = mysql.connector.connect(
            host="localhost", user="jarwallc_admin", passwd="nateglass@1551", database="jarwallc_sngpl_main")
        searchCursor = searchdb.cursor(dictionary=True)
        searchCursor.execute(f"SELECT * FROM `{tbsn}`")
        all_data = searchCursor.fetchall()
        subData = []
        count = 0
        if value == "full":
            subData = all_data
        else:
            for indexVal in range(len(all_data), 0, -1):
                if count == int(value):
                    break
                subData.append(all_data[indexVal - 1])
                count += 1
        subData[0]["time"] = str(subData[0]["time"]).split(", ")[0]
        pressure = subData[0]["pressure"]
        status = subData[0]["status"]
        setPres = subData[0]["setPresssure"]
        searchCursor.execute(
            f"INSERT INTO `{tbsn}` (`pressure`, `status`, `setPresssure`) VALUES ('{pres}', '{status}', '{setPres}')")
        return "pressure update"
    else:
        return "error occured"


@app.route('/v/aja/sngpl/<token>&tbs=<tbsn>', methods=['GET', 'POST'])
def v_aja_sngpl_main(token, tbsn):
    if str(token) in "ajkER8ERNFNJmxngnxcgiuNSJFDGGORTFEser888er":
        value = "1"
        searchdb = mysql.connector.connect(
            host="localhost", user="jarwallc_admin", passwd="nateglass@1551", database="jarwallc_sngpl_main")
        searchCursor = searchdb.cursor(dictionary=True)
        searchCursor.execute(f"SELECT * FROM `{tbsn}`")
        all_data = searchCursor.fetchall()
        subData = []
        count = 0
        if value == "full":
            subData = all_data
        else:
            for indexVal in range(len(all_data), 0, -1):
                if count == int(value):
                    break
                subData.append(all_data[indexVal - 1])
                count += 1
        subData[0]["time"] = str(subData[0]["time"]).split(", ")[0]
        pressure = subData[0]["pressure"]
        status = subData[0]["status"]
        setPres = subData[0]["setPresssure"]
        try:
            setVal = request.form["set"]
            searchCursor.execute(
                f"INSERT INTO `{tbsn}` (`pressure`, `status`, `setPresssure`) VALUES ('{pressure}', '{status}', '{setVal}')")
        except:
            setVal = request.form["stat"]
            searchCursor.execute(
                f"INSERT INTO `{tbsn}` (`pressure`, `status`, `setPresssure`) VALUES ('{pressure}', '{setVal}', '{setPres}')")
        return "Success"
    else:
        return "Failed"


@app.route('/v/aja/sngpl_get/<token>&tbs=<tbsn>', methods=['GET', 'POST'])
def v_aja_get_sngpl(token, tbsn):
    value = "1"
    if token == "ajkER8ERNFNJmxngnxcgiuNSJFDGGORTFEser888er":
        searchdb = mysql.connector.connect(
            host="localhost", user="jarwallc_admin", passwd="nateglass@1551", database="jarwallc_sngpl_main")
        searchCursor = searchdb.cursor(dictionary=True)
        searchCursor.execute(f"SELECT * FROM `{tbsn}`")
        all_data = searchCursor.fetchall()
        subData = []
        count = 0
        if value == "full":
            subData = all_data
        else:
            for indexVal in range(len(all_data), 0, -1):
                if count == int(value):
                    break
                subData.append(all_data[indexVal - 1])
                count += 1
        subData[0]["time"] = str(subData[0]["time"]).split(", ")[0]
        result = {f"{tbsn}": subData, "success": "1"}
        return str(result)
    else:
        return "You are not allowed to view the content"
