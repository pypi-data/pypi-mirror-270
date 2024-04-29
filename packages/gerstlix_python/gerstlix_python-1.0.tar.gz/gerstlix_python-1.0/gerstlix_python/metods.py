import requests

acceptServers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,101,102,103,201,202,203,204,205,206,207]
acceptServersArz = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
acceptProject = ['arz', 'marz','rrp']


class gerstlixAPI():
    def __init__(self, token:str=None):
        self.token = token

    def check_work_methods(self):
        list = ["utils.geoIp","server.getStatus","server.getRecords","server.getRecord","server.getMinistersList","server.getMinister","server.getLeadersList","server.getLeader","server.getDeputyList","server.getDeputy","game.getRichPlayers","game.getOldPlayers","game.getMembers","game.getGhettoMap"]
        status = []
        for i in list:
            r = requests.get(f"https://api2.gerstlix.com/v1/{i}")
            status.append({i:"ok" if r.status_code == 500 else "fail"})
        return status

    def count_methods(self):
        return (len(dir(self)) - len(dir(object)))-4

    def get_ip(self, ip=None):
        if ip != None:
            r = requests.get(f"https://api2.gerstlix.com/v1/utils.geoIp/?token={self.token}&ip={ip}")
            return r.json()
        else:
            return {"status": "fail", "message":"Укажите параметры!"}

    def get_player(self, server:int=None, player:str=None):
        if server in acceptServersArz and server != None:
            if player != None and isinstance(player, str) == True:
                r = requests.get(f"https://api2.gerstlix.com/v1/game.getPlayer/?token={self.token}&server={server}&player={player}")
                return r.json()   
            else:
                return "Проверьте валидность player"
        else:
            return f"Сервер: {server} не находится в одобренном списке [only ARZ]"

    def get_info(self, server:int=None):
        if server in acceptServers and server != None:
            r = requests.get(f"https://api2.gerstlix.com/v1/server.getInfo/?token={self.token}&server={server}")
            return r.json()
        else:
            return f"Сервер: {server} не находится в одобренном списке"

        
    def get_status(self, gameProject:str=None):
        if gameProject in acceptProject:
            r = requests.get(f"https://api2.gerstlix.com/v1/server.getStatus/?token={self.token}")
            data = r.json()
            if data['success']:
                if gameProject == "arz":
                    arz = data['data']['Arizona RP']
                    result = []
                    for i in arz:
                        result.append({"serverNumber": i['serverNumber'],"serverName": i['serverName'],"online": i['online'],"maxPlayers": i['maxPlayers'],"password": i['password'],"vkGroup": i['vkGroup'],"gerstlixLeaders": i['gerstlixLeaders'],"gerstlixGamePanel": i['gerstlixGamePanel'],"gerstlixCourt": i['gerstlixCourt']})
                elif gameProject == "marz":
                    marz = data['data']['Arizona Mobile']
                    result = []
                    for i in marz:
                        result.append({"serverNumber": i['serverNumber'],"serverName": i['serverName'],"online": i['online'],"maxPlayers": i['maxPlayers'],"password": i['password'],"vkGroup": i['vkGroup'],"gerstlixLeaders": i['gerstlixLeaders'],"gerstlixGamePanel": i['gerstlixGamePanel'],"gerstlixCourt": i['gerstlixCourt']})
                elif gameProject == "rrp":
                    rrp = data['data']['Rodina RP']
                    result = []
                    for i in rrp:
                        result.append({"serverNumber": i['serverNumber'],"serverName": i['serverName'],"online": i['online'],"maxPlayers": i['maxPlayers'],"password": i['password'],"vkGroup": i['vkGroup'],"gerstlixLeaders": i['gerstlixLeaders'],"gerstlixGamePanel": i['gerstlixGamePanel'],"gerstlixCourt": i['gerstlixCourt']})
                return result  
            else:
                return {"status":"fail", "errorMessage": data['message']}
        else:
            return {"status":"fatal error", "errorMessage": f"Укжите gameProject: {acceptProject}"}
        
    def get_records(self, server:int=None):
        if server in acceptServers:
            r = requests.get(f"https://api2.gerstlix.com/v1/server.getRecords/?token={self.token}&server={server}")
            return r.json()
        else:
            return f"Сервер: {server} не находится в одобренном списке"
    
    def get_record_fraction(self, server:int=None, fractionId:int=None):
        if server != None and server in acceptServers:
            r = requests.get(f"https://api2.gerstlix.com/v1/server.getRecord/?token={self.token}&server={server}&fraction={fractionId}")
            return r.json()
        else:
            return f"Сервер: {server} не находится в одобренном списке"

    def get_minister_list(self, server:int=None):
        if server != None and server in acceptServers:
            r = requests.get(f"https://api2.gerstlix.com/v1/server.getMinistersList/?token={self.token}&server={server}")
            return r.json()
        else:
            return f"Сервер: {server} не находится в одобренном списке"

    def get_minister(self, server:int=None, fractionId:int=None):
        if fractionId != None and server != None and server in acceptServers:
            r = requests.get(f"https://api2.gerstlix.com/v1/server.getMinister/?token={self.token}&server={server}&fraction={fractionId}")
            return r.json()
        else:
            return f"Проверьте serverID и fractionID на валидность"

    def get_leaders(self, server:int=None):
        if server != None and server in acceptServers:
            r = requests.get(f"https://api2.gerstlix.com/v1/server.getLeadersList/?token={self.token}&server={server}")
            return r.json()
        else:
            return f"Сервер: {server} не находится в одобренном списке"
        
    def get_leader(self, server:int=None, fractionId:int=None):
        if server != None and server in acceptServers and fractionId != None:
            r = requests.get(f"https://api2.gerstlix.com/v1/server.getLeader/?token={self.token}&server={server}&fraction={fractionId}")
            return r.json()
        else:
            return f"Проверьте serverID и fractionID на валидность"

    def get_deputies(self, server: int = None):
        if server in acceptServers and server is not None:
            r = requests.get(f"https://api2.gerstlix.com/v1/server.getDeputyList/?token={self.token}&server={server}")
            return r.json()
        else:
            return f"Сервер: {server} не находится в одобренном списке"

    def get_deputy(self, server:int=None, fractionId:int=None):
        if server != None and server in acceptServers and fractionId != None:
            r = requests.get(f"https://api2.gerstlix.com/v1/server.getDeputy/?token={self.token}&server={server}&fraction={fractionId}")
            return r.json()
        else:
            return f"Проверьте serverID и fractionID на валидность"

    def get_rich_players(self, server:int=None):
        if server != None and server in acceptServers:
            r = requests.get(f"https://api2.gerstlix.com/v1/game.getRichPlayers/?token={self.token}&server={server}")
            return r.json()
        else:
            return f"Сервер: {server} не находится в одобренном списке"

    def get_old_players(self, server:int=None):
        if server != None and server in acceptServers:
            r = requests.get(f"https://api2.gerstlix.com/v1/game.getOldPlayers/?token={self.token}&server={server}")
            return r.json()
        else:
            return f"Сервер: {server} не находится в одобренном списке"
        
    def get_members(self, server:int=None, fractionId:int=None):
        closedServers = [201,202,203,204,205,206]
        if server != None and server in acceptServers and server not in closedServers and fractionId != None:
            r = requests.get(f"https://api2.gerstlix.com/v1/game.getMembers/?token={self.token}&server={server}&fraction={fractionId}")
            return r.json()
        else:
            return f"Проверьте serverID и fractionID на валидность"

    def get_admins_list(self, server:int=None):
        if server != None:
            r = requests.get(f"https://api2.gerstlix.com/v1/server.getAdminsList/?token={self.token}&server={server}")
            return r.json()
        else:
            return f"Введите server"
    def get_ghetto_territories(self, server:int=None):
        if server != None and server in acceptServers:

            r = requests.get(f"https://api2.gerstlix.com/v1/game.getGhettoMap/?token={self.token}&server={server}")
            data = r.json()

            if data['success']:
                territory_counts = {}
                for territory in data['data']['territories']:
                    if territory in territory_counts:
                        territory_counts[territory] += 1
                    else:
                        territory_counts[territory] = 1
                territory_names = {11: 'Grove Street',12: 'Vagos',13: 'Ballas',14: 'Aztecas',15: 'Rifa',25: 'Wolfs'}
                terrs = []
                for i, k in territory_counts.items():
                    territory_name = territory_names.get(i, 'Неизвестная территория')
                    terrs.append({"name": territory_name, "count": k})

                return {
                    "serverId": data['data']['serverId'],
                    "serverName": data['data']['serverName'],
                    "lastUpdated": data['data']['lastUpdated'],
                    "terrs": terrs
                }
            else:
                return {"status": "fail", "errorMessage": data['message']}
        else:
            return f"Сервер: {server} не находится в одобренном списке"