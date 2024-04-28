import datetime
import urllib.parse
from typing import Iterable, Union
from .functions import get_request, explain_enchant
from .METADATA import SERVER_NAME_2_ID, CHARACTER_SEARCH_NAME, CHARACTER_INFORMATION_NAME, STATUS_NAME, EQUIPMENT_LIST, AVATAR_LIST, PLATINUM_AVATAR_LIST

__all__ = [
    "CharacterSearch",
    "CharacterInformation",
    "Timeline",
    "Status",
    "Equipments",
    "Avatars",
    "Creature",
    "Flag",
    "Talismans",
    "EquipmentTrait",
    "SkillStyle",
    "Buff",
    "CharacterFame"
]

class PyNeople():
    """
    부모 Class로 사용
    """
    def __init__(self, arg_api_key : str):
        """
        클래스 생성 시 Neople Open API key를 입력받는다
            Args :
                arg_api_key(str) : Neople Open API key
        """        
        self._api_key = arg_api_key

class CharacterSearch(PyNeople):
    """
    Neople Open API 02. 캐릭터 검색
    """

    def __init__(self, arg_api_key : str):
        super().__init__(arg_api_key)

    def get_data(self, arg_server_name : str, arg_character_name : str):
        """
        서버 이름과 캐릭터 이름을 검색하면 기본 정보를 반환
            Args : 
                arg_server_name(str) : 서버 이름  ex) 디레지에, diregie
                
                arg_character_name(str) : 캐릭터 이름 ex) 홍길동
        """
        
        # 한글 서버명을 영문 서버명으로 변환, 영문 서버명은 그대로 입력, 그 외의 입력은 에러 발생
        if arg_server_name in SERVER_NAME_2_ID.keys():
            arg_server_name = SERVER_NAME_2_ID[arg_server_name]
        elif arg_server_name in SERVER_NAME_2_ID.values():
            pass
        else:
            raise ValueError("서버 이름을 확인하시오")
        self._server_id = arg_server_name
        url = f"https://api.neople.co.kr/df/servers/{arg_server_name}/characters?characterName={urllib.parse.quote(arg_character_name)}&limit=1&apikey={self._api_key}"
        
        # parse_data에 매개변수로 사용 될 것을 생각해서 dict를 받을 수 있도록 정보 다듬어서 제공
        try:
            return get_request(url).get("rows")[0]
        except IndexError:
            return dict()
    
    def parse_data(self, arg_data : dict, attribute_list : Iterable[str] = CHARACTER_SEARCH_NAME.keys()):
        """
        데이터를 정리해서 하위 속성에 저장
            Args :
                arg_data(dict) : Neople Open API 를 통해 받은 data
                attribute_list(iterable of str) : 원하는 하위 속성 명
        """
        # 하위 속성에 데이터 할당
        for attribute_name in attribute_list:            
            setattr(self, attribute_name, arg_data.get(CHARACTER_SEARCH_NAME[attribute_name]))


class CharacterInformation(PyNeople):
    """
    Neople Open API 03. 캐릭터 '기본정보' 조회
    """

    def __init__(self, arg_api_key : str):
        super().__init__(arg_api_key)
    
    def get_data(self, arg_server_id : str, arg_character_id : str):
        """
        영문 서버 이름과 캐릭터 ID 를 검색하면 기본 정보를 반환
            Args : 
                arg_server_id(str) : 영문 서버 이름  ex) diregie
                
                arg_character_name(str) : 캐릭터 ID ex) 80d9189c86147ab9a7b8c1481be85d95
        """    
        self._server_id = arg_server_id
        url = f"https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}?apikey={self._api_key}"
        return get_request(url)
    
    def parse_data(self, arg_data : dict, attribute_list : Iterable[str] = CHARACTER_INFORMATION_NAME.keys()):
        """
        데이터를 정리해서 하위 속성에 저장
            Args :
                arg_data(dict) : Neople Open API 를 통해 받은 data
                attribute_list(iterable of str) : 원하는 하위 속성 명
        """
        # 하위 속성에 데이터 할당
        for attribute_name in attribute_list:
            setattr(self, attribute_name, arg_data.get(CHARACTER_INFORMATION_NAME[attribute_name]))


class Timeline(PyNeople):
    """
    Neople Open API 04. 캐릭터 '타임라인 정보' 조회
    """    

    def __init__(self, arg_api_key : str):
        super().__init__(arg_api_key)
    
    def get_data(self, 
                 arg_server_id : str, 
                 arg_character_id : str, 
                 arg_end_date : str, 
                 arg_last_end_date : str = "2017-09-21 00:00", 
                 arg_last_end_data : Union[dict, None] = None, 
                 arg_limit : int = 100, 
                 arg_code : Union[int, str] = "",
                 arg_print_log : bool = False):
        """
        서버ID와 캐릭터ID 원하는 수집시간(arg_end_date)을 입력받으면 타임라인데이터를 반환한다.
            Args :
                arg_server_id(str) : 서버ID ex) cain
                
                arg_character_id(str) : 캐릭터ID ex) 80d9189c86147ab9a7b8c1481be85d95
                
                arg_end_date(str) : 이 시간까지 수집을 한다 ex) 2023-03-03 15:57
                
                arg_last_end_date(str) : 이 시간부터 수집을 한다 ex) 2018-03-03 15:57
                
                arg_last_end_data(dict) : 지금까지 수집한 해당 캐릭터의 마지막 타임라인 데이터
                
                arg_limit(int) : 한번 request할 때 수집 할 타임라인 데이터의 개수
                
                arg_code(int) : 수집하고 싶은 타임라인 코드 ex)201, 202 참조) https://developers.neople.co.kr/contents/guide/pages/all 
                
                arg_print_log(boolean) : 데이터 수집의 과정의 print 여부   
        """
        self._server_id = arg_server_id
        timeline = []
        
        end_date = datetime.datetime.strptime(arg_end_date, '%Y-%m-%d %H:%M')
        start_date = end_date - datetime.timedelta(days=90)
        if start_date < datetime.datetime.strptime(arg_last_end_date, '%Y-%m-%d %H:%M'):
            start_date = datetime.datetime.strptime(arg_last_end_date, '%Y-%m-%d %H:%M')
        next = ""
        while start_date < end_date:
            stop = False
            url = f"""https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}/timeline?limit={arg_limit}&code={arg_code}&startDate={start_date.strftime('%Y-%m-%d %H:%M')}&endDate={end_date.strftime('%Y-%m-%d %H:%M')}&next={next}&apikey={self._api_key}"""
            if arg_print_log:
                print(f"서버 = {arg_server_id}, 캐릭터 = {arg_character_id} 시작 = {start_date.strftime('%Y-%m-%d %H:%M')}, 끝 = {end_date.strftime('%Y-%m-%d %H:%M')}")
            data = get_request(url)
            next = data['timeline']['next']

            # 데이터가 있다면
            if data['timeline']['rows']:                 
                for log in data['timeline']['rows']:
                    if log == arg_last_end_data:
                        stop = True
                        break
                    else:
                        timeline.append(log)
                # 마지막으로 수집된 타임라인 데이터와 일치하는 항목이 있다면
                if stop:
                    break        

            # 타임라인데이터가 있고 마지막 로그가 캐릭터 생성이라면
            if timeline and timeline[-1]['code'] == 101:
                print("캐릭터 생성 로그를 확인했습니다")
                break

            # 해당기간에 next 데이터가 있으면
            if next:
                continue
            # 해당기간에 next 없으면
            else:
                end_date = start_date
                start_date = end_date - datetime.timedelta(days=90)
                if start_date < datetime.datetime.strptime(arg_last_end_date, '%Y-%m-%d %H:%M'):
                    start_date = datetime.datetime.strptime(arg_last_end_date, '%Y-%m-%d %H:%M')
                next = ""    
                continue
        return timeline

class Status(PyNeople):
    """
    Neople Open API 05. 캐릭터 '능력치 정보' 조회
    """    

    def __init__(self, arg_api_key : str):
        super().__init__(arg_api_key)

    def get_data(self, arg_server_id : str, arg_character_id : str):
        """
        캐릭터의 모험단명부터 명성 등 정보를 반환한다
            Args:
                arg_server_id(str) :  서버 ID
                
                arg_character_id(str) : 캐릭터 ID
        """
        self._server_id = arg_server_id
        url = f'https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}/status?apikey={self._api_key}'
        return get_request(url)
    def parse_data(self, arg_data : dict, attribute_list : Iterable[str] = STATUS_NAME.keys()):
        """
        데이터를 정리해서 하위 attribute에 저장
            Args :
                arg_data(dict) : Neople Open API 를 통해 받은 data
                attribute_list(iterable of str) : 원하는 하위 속성 명
        """
        
        # 모험단, 길드 버프 정리
        if arg_data.get('buff'):
            for buff in arg_data['buff']:
                if buff.get('name') == '모험단 버프':
                    arg_data['adventure_level'] = buff.get('level')
                elif buff.get('name') == '무제한 길드능력치':
                    arg_data['unlimited_guild_abilities'] = True
                elif buff.get('name') == '기간제 길드능력치':
                    arg_data['limited_guild_abilities'] = True
                else:
                    pass
        
        # 상세 스탯 정리
        if arg_data.get('status'):
            for item in arg_data['status']:
                arg_data[item['name']] = item['value']   
        
        # 하위 속성에 데이터 할당
        for attribute_name in attribute_list:
            setattr(self, attribute_name, arg_data.get(STATUS_NAME[attribute_name]))

class OptionInfo():
    """
    Equipments를 위해 사용되는 Class
    """

    def __init__(self):
        self.explain = None
    
    def get_option_info_data(self, arg_option_info_dict : dict):
        self.explain = arg_option_info_dict.get('explain').replace("'", "") # 얼음 땡 옵션 예외처리를 위한 replace    

class GrowInfo():
    """
    Equipments를 위해 사용되는 Class
    """    

    def __init__(self):
        self.level = None       # 장비 성장 레벨
        self.exp_rate = None    # 장비 성장 경험치
        self.transfer = None    # 전송 받은 옵션
        self.option_1 = None    # 1옵션
        self.option_2 = None    # 2옵션
        self.option_3 = None    # 3옵션
        self.option_4 = None    # 4옵션

    def get_grow_info_data(self, arg_grow_info_dict : dict):
        self.level = arg_grow_info_dict.get('level')
        self.exp_rate = arg_grow_info_dict.get('expRate', 0)
        if arg_grow_info_dict.get('options'):
            for i, option in enumerate(arg_grow_info_dict.get('options')):
                if option.get('transfer') == True:
                    setattr(self, 'transfer', i+1)
                else:
                    pass    
                setattr(self, f'option_{i+1}', option.get('explain')) 

class Equipment():
    """
    Equipments를 위해 사용되는 Class
    """

    def __init__(self):
        self.item_name = None
        self.item_available_level = None
        self.item_rarity = None
        self.reinforce = None
        self.item_grade_name = None
        self.enchant = None
        self.amplification_name = None
        self.refine = None
        self.upgrade_info = None
        self.mist_gear = None
        self.grow_info = GrowInfo()
    
    def get_equipment_data(self, arg_equipment_dict : dict):
        self.item_name = arg_equipment_dict.get('itemName') # 이름
        self.item_available_level = arg_equipment_dict.get('itemAvailableLevel') # 레벨 제한
        self.item_rarity = arg_equipment_dict.get('itemRarity') # 레어도
        self.reinforce = arg_equipment_dict.get('reinforce') # 강화수치             
        self.amplification_name = arg_equipment_dict.get('amplificationName') # 차원의 기운 여부 ex 차원의 힘, 차원의 지능, None
        self.refine = arg_equipment_dict.get('refine') # 제련   
        self.item_grade_name = arg_equipment_dict.get('itemGradeName') # 등급(최상~최하)
        self.enchant = explain_enchant(arg_equipment_dict.get('enchant')) # 마법부여

        # 미스트 기어 정보
        if arg_equipment_dict.get('mistGear'):
            self.mist_gear = 'mist_gear'
        elif arg_equipment_dict.get('pureMistGear'):
            self.mist_gear = 'pure_mist_gear'   
        elif arg_equipment_dict.get('refinedMistGear'):
            self.mist_gear = 'refined_mistgear'                   
        else :
            pass    


        if arg_equipment_dict.get("upgradeInfo"):
            self.upgrade_info = arg_equipment_dict.get("upgradeInfo").get('itemName') # 융합장비
        
        # 105제 성장 장비 정보
        if arg_equipment_dict.get("customOption"):
            self.grow_info.get_grow_info_data(arg_equipment_dict.get('customOption'))
        elif arg_equipment_dict.get("fixedOption"):
            self.grow_info.get_grow_info_data(arg_equipment_dict.get("fixedOption"))
        else :
            pass

class BakalInfo():
    """
    Equipments를 위해 사용되는 Class
    """

    def __init__(self):
        self.option_1 = None
        self.option_2 = None
        self.option_3 = None

    def get_bakal_info_data(self, arg_bakal_info_dict):
        if arg_bakal_info_dict.get('options'):
            for i, option in enumerate(arg_bakal_info_dict.get('options')):
                setattr(self, f'option_{i+1}',option.get('explain'))                

class Weapon(Equipment):
    """
    Equipments를 위해 사용되는 Class
    """

    def __init__(self):
        super().__init__()
        self.bakal_info = BakalInfo()

    def get_equipment_data(self, arg_equipment_dict):
        super().get_equipment_data(arg_equipment_dict)
        self.bakal_info.get_bakal_info_data(arg_equipment_dict.get("bakalInfo", dict())) # 바칼 무기 융합


class Equipments(PyNeople):
    """
    Neople Open API 06. 캐릭터 '장착 장비' 조회
    """    

    def __init__(self, arg_api_key : str):
        super().__init__(arg_api_key)

    def get_data(self, arg_server_id : str, arg_character_id : str):
        """
        영문 서버 이름과 캐릭터 ID 를 검색하면 장착 장비 정보를 반환
            Args : 
                arg_server_id(str) : 영문 서버 이름  ex) diregie
                
                arg_character_name(str) : 캐릭터 ID ex) 80d9189c86147ab9a7b8c1481be85d95
        """        
        self._server_id = arg_server_id
        url = f'https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}/equip/equipment?apikey={self._api_key}'
        return get_request(url)

    def parse_data(self, arg_data : dict):
        """
        데이터를 정리해서 하위 attribute에 저장
            Args :
                arg_data(dict) : Neople Open API 를 통해 받은 data
        """
        # 하위 속성 생성
        for equipment in EQUIPMENT_LIST:
            if equipment == 'weapon':
                setattr(self, equipment, Weapon())
            else:
                setattr(self, equipment, Equipment())
                
        # 장착 장비 정보 할당        
        for equipment in arg_data.get('equipment', list()):
            getattr(self, equipment['slotId'].lower()).get_equipment_data(equipment)
            # setattr(self, equipment['slotId'].lower(), equipment_data)
        
        # 세트 아이템 정보 할당
        if arg_data.get('setItemInfo'):
            set_item_info_list = []
            for set_item_info in arg_data.get('setItemInfo'):
                set_item_name_list = set_item_info.get('setItemName').split()
                set_item_name_list.insert(-1, f"{set_item_info.get('activeSetNo')}")
                set_item_info_list.append(" ".join(set_item_name_list))
            setattr(self, 'set_item_info', ", ".join(set_item_info_list))
        else:
            setattr(self, 'set_item_info', None)


class Avatar():
    """
    Avatars를 위해 사용되는 Class
    """

    def __init__(self):
        self.item_name = None       # 아바타 이름
        self.item_rarity = None     # 아바타 레어도
        self.option_ability = None  # 아바타 옵션
        self.emblem_1 = None        # 엠블렘1 옵션
        self.emblem_2 = None        # 엠블렘2 옵션
        
    def get_avatar_data(self, arg_avatar_dict):
        self.item_name = arg_avatar_dict.get("itemName")
        self.item_rarity = arg_avatar_dict.get("itemRarity")
        self.option_ability = arg_avatar_dict.get("optionAbility")
        for i, emblem in enumerate(arg_avatar_dict.get('emblems', dict())):
            setattr(self, f'emblem_{i+1}', emblem.get('itemName'))

class PlatinumAvatar(Avatar):
    """
    Avatars를 위해 사용되는 Class
    """   

    def __init__(self):
        super().__init__()
        self.emblem_3 = None # 플래티넘 엠블렘 옵션

    def get_avatar_data(self, arg_avatar_dict):
        super().get_avatar_data(arg_avatar_dict)

class Avatars(PyNeople):
    """
    Neople Open API 07. 캐릭터 '장착 아바타' 조회
    """       

    def __init__(self, arg_api_key: str):
        super().__init__(arg_api_key)

    def get_data(self, arg_server_id: str, arg_character_id : str):    
        """
        영문 서버 이름과 캐릭터 ID 를 검색하면 장착 아바타 정보를 반환
            Args : 
                arg_server_id(str) : 영문 서버 이름  ex) diregie
                
                arg_character_name(str) : 캐릭터 ID ex) 80d9189c86147ab9a7b8c1481be85d95
        """        
        self._server_id = arg_server_id
        url = f'https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}/equip/avatar?apikey={self._api_key}'
        return get_request(url)

    def parse_data(self, arg_data : dict):
        """
        데이터를 정리해서 하위 attribute에 저장
            Args :
                arg_data(dict) : Neople Open API 를 통해 받은 data
        """        
        # 하위 속성 생성
        for avatar in AVATAR_LIST:
            if avatar in PlatinumAvatar:
                setattr(self, avatar, PlatinumAvatar())    
            else:
                setattr(self, avatar, Avatar())
        
        # 하위 속성에 데이터 할당
        for avatar in arg_data.get('avatar', list()):
            getattr(self, f'{avatar["slotId"].lower()}').get_avatar_data(avatar)


class Creature(PyNeople):
    """
    Neople Open API 08. 캐릭터 '장착 크리쳐' 조회
    """
    
    def __init__(self, arg_api_key: str):
        super().__init__(arg_api_key)
        
    def get_data(self, arg_server_id : str, arg_character_id : str):
        """
        영문 서버 이름과 캐릭터 ID 를 검색하면 장착 크리쳐 정보를 반환
            Args : 
                arg_server_id(str) : 영문 서버 이름  ex) diregie
                
                arg_character_name(str) : 캐릭터 ID ex) 80d9189c86147ab9a7b8c1481be85d95
        """
        self._server_id = arg_server_id
        url = f"https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}/equip/creature?apikey={self._api_key}"
        return get_request(url)
    
    def parse_data(self, arg_data : dict):
        """
        데이터를 정리해서 하위 attribute에 저장
            Args :
                arg_data(dict) : Neople Open API 를 통해 받은 data
        """        
        self.creature = arg_data.get('creature', dict()).get('itemName')
        
class Flag(PyNeople):
    """
    Neople Open API 09. 캐릭터 '장착 휘장' 조회
    """

    def __init__(self, arg_api_key: str):
        super().__init__(arg_api_key)
    
    def get_data(self, arg_server_id : str, arg_character_id : str):
        """
        영문 서버 이름과 캐릭터 ID 를 검색하면 장착 휘장 정보를 반환
            Args : 
                arg_server_id(str) : 영문 서버 이름  ex) diregie
                
                arg_character_name(str) : 캐릭터 ID ex) 80d9189c86147ab9a7b8c1481be85d95
        """        
        self._server_id = arg_server_id
        url = f"https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}/equip/flag?apikey={self._api_key}"
        return get_request(url)
    
    def parse_data(self, arg_data):
        """
        데이터를 정리해서 하위 attribute에 저장
            Args :
                arg_data(dict) : Neople Open API 를 통해 받은 data
        """        
        self.gem_1 = None       # 젬1 레어도
        self.gem_2 = None       # 젬2 레어도
        self.gem_3 = None       # 젬3 레어도
        self.gem_4 = None       # 젬4 레어도
        self.item_rarity = arg_data.get('flag', dict()).get('itemRarity')   # 휘장 레어도
        self.reinforce = arg_data.get('flag', dict()).get('reinforce')      # 휘장 강화 수치
        for i, gem in enumerate(arg_data.get('flag', dict()).get('gems', list())):
            setattr(self, f"gem_{i+1}", gem.get("itemRarity"))

class Talisman():
    """
    Talismans를 위해 사용되는 Class 
    """

    def __init__(self):
        self.item_name = None
        self.rune_1 = None
        self.rune_2 = None
        self.rune_3 = None   
    def get_talisman_data(self, arg_talisman_data):
        self.item_name = arg_talisman_data.get('talisman', dict()).get('itemName')
        for i, rune in enumerate(arg_talisman_data.get('runes', list())):
            setattr(self, f'rune_{i+1}', rune.get('itemName'))        

class Talismans(PyNeople):
    """
    Neople Open API 10. 캐릭터 '장착 탈리스만' 조회
    """ 
    def __init__(self, arg_api_key: str):
        super().__init__(arg_api_key)

    def get_data(self, arg_server_id : str, arg_character_id : str):
        """
        영문 서버 이름과 캐릭터 ID 를 검색하면 장착 탈리스만 정보를 반환
            Args : 
                arg_server_id(str) : 영문 서버 이름  ex) diregie
                
                arg_character_name(str) : 캐릭터 ID ex) 80d9189c86147ab9a7b8c1481be85d95
        """                
        self._server_id = arg_server_id
        url = f"https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}/equip/talisman?apikey={self._api_key}"         
        return get_request(url)
    
    def parse_data(self, arg_data : dict):
        """
        데이터를 정리해서 하위 attribute에 저장
            Args :
                arg_data(dict) : Neople Open API 를 통해 받은 data
        """        
        for i, talisman in enumerate(arg_data.get("talismans", list())):
            setattr(self, f"talisman_{i+1}", Talisman())
            getattr(self, f"talisman_{i+1}").get_talisman_data(talisman)        


class EquipmentTrait(PyNeople):
    """
    Neople Open API 11. 캐릭터 '장비 특성' 조회
    """ 

    def __init__(self, arg_api_key: str):
        super().__init__(arg_api_key)

    def get_data(self, arg_server_id : str, arg_character_id : str):
        """
        영문 서버 이름과 캐릭터 ID 를 검색하면 장비 특성 정보를 반환
            Args : 
                arg_server_id(str) : 영문 서버 이름  ex) diregie
                
                arg_character_name(str) : 캐릭터 ID ex) 80d9189c86147ab9a7b8c1481be85d95
        """                
        self._server_id = arg_server_id
        url = f"https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}/equip/equipment-trait?apikey={self._api_key}"
        return get_request(url)
    
    def parse_data(self, arg_data : dict):
        """
        데이터를 정리해서 하위 attribute에 저장
        강력한 일격과 명상의 레벨만 확인
            Args :
                arg_data(dict) : Neople Open API 를 통해 받은 data
        """

        self.total_point = arg_data.get("equipmentTrait", dict()).get("total", dict()).get("point")
        self.category_name = arg_data.get("equipmentTrait", dict()).get("category", dict()).get("name")
        self.strong_hit_level = 0
        self.meditation_level = 0
        option_list = arg_data.get("equipmentTrait", dict()).get("options", list())
        option_list = list(filter(lambda x : x.get("name") in ["[강력한 일격]", "[명상]"], option_list))
        for option in option_list:
            if option.get("name") == "[강력한 일격]":
                self.strong_hit_level = option.get("level")
            else:
                self.meditation_level = option.get("level")


class SkillStyle(PyNeople):
    """
    Neople Open API 12. 캐릭터 '스킬 스타일' 조회
    """ 

    def __init__(self, arg_api_key: str):
        super().__init__(arg_api_key)

    def get_data(self, arg_server_id : str, arg_character_id : str):
        """
        영문 서버 이름과 캐릭터 ID 를 검색하면 스킬 스타일 정보를 반환
            Args : 
                arg_server_id(str) : 영문 서버 이름  ex) diregie
                
                arg_character_name(str) : 캐릭터 ID ex) 80d9189c86147ab9a7b8c1481be85d95
        """                
        self._server_id = arg_server_id
        url = f"https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}/skill/style?apikey={self._api_key}"
        return get_request(url)

    def parse_data(self, arg_data : dict):
        """
        데이터를 정리해서 하위 attribute에 저장
        스킬 코드만 구현 완료 나머지 추후 개발
            Args :
                arg_data(dict) : Neople Open API 를 통해 받은 data
        """        

        self.skill_code = arg_data.get("skill", dict()).get("hash")

class BuffAvatar():
    """
    Buff를 위해 사용되는 Class
    """
    def __init__(self):
        self.item_name = None
    def get_buff_avatar_data(self, arg_avatar_dict):
        try: 
            self.item_name = arg_avatar_dict['itemName']
        except:
            pass

class BuffPlatimun(BuffAvatar):
    """
    Buff를 위해 사용되는 Class
    """    
    def __init__(self):
        super().__init__()    
        self.option = None
        self.platinum = None
    
    def get_buff_avatar_data(self, arg_avatar_dict):
        super().get_buff_avatar_data(arg_avatar_dict)
        self.option = arg_avatar_dict.get('optionAbility')
        if arg_avatar_dict.get('emblems'):
            for emblems in arg_avatar_dict.get('emblems'):
                if emblems.get('slotColor') == '플래티넘':
                    self.platinum = emblems.get('itemName')


class Buff(PyNeople):
    """
    Neople Open API 13. 캐릭터 "버프 스킬 강화 장착 장비" 조회
    Neople Open API 14. 캐릭터 "버프 스킬 강화 장착 아바타" 조회
    Neople Open API 15. 캐릭터 "버프 스킬 강화 장착 크리쳐" 조회
    """

    def __init__(self, arg_api_key: str):
        super().__init__(arg_api_key)
         
    def get_data(self, arg_server_id : str, arg_character_id : str):
        """
        영문 서버 이름과 캐릭터 ID 를 검색하면 버프 강화(장비, 아바타, 크리쳐) 정보를 반환
            Args : 
                arg_server_id(str) : 영문 서버 이름  ex) diregie
                
                arg_character_name(str) : 캐릭터 ID ex) 80d9189c86147ab9a7b8c1481be85d95
        """   
        self._server_id = arg_server_id
        buff_info_dict = {}     
        buff_equipment_data = get_request(f"https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}/skill/buff/equip/equipment?apikey={self._api_key}")
        buff_avatar_data = get_request(f"https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}/skill/buff/equip/avatar?apikey={self._api_key}")
        buff_creature_data = get_request(f"https://api.neople.co.kr/df/servers/{arg_server_id}/characters/{arg_character_id}/skill/buff/equip/creature?apikey={self._api_key}")
        buff_info_dict["equipment"] = buff_equipment_data
        buff_info_dict["avatar"] = buff_avatar_data
        buff_info_dict["creature"] = buff_creature_data
        return buff_info_dict

    def parse_data(self, arg_data : dict):
        """
        데이터를 정리해서 하위 attribute에 저장
            Args :
                arg_data(dict) : Neople Open API 를 통해 받은 data
        """         
        # 하위 속성 생성
        self.buff_level = None
        self.buff_desc = None
        for equipment in EQUIPMENT_LIST:
            setattr(self, f"self.buff_equipment_{equipment}", None)
        for avatar in list(set(AVATAR_LIST) - set(PLATINUM_AVATAR_LIST)):
            setattr(self, f"self.buff_avatar_{avatar}", BuffAvatar())
        for avatar in PLATINUM_AVATAR_LIST:
            setattr(self, f"self.buff_avatar_{avatar}", BuffPlatimun())
        self.buff_creature = None  
        
        arg_data["equipment"] = arg_buff_equipment_data
        arg_data["avatar"] = arg_buff_avatar_data
        arg_data["creature"] = arg_buff_creature_data

        if arg_buff_equipment_data.get("skill", dict()).get('buff'):
            arg_buff_equipment_data = arg_buff_equipment_data.get("skill", dict()).get('buff')
            # 버프 강화 장비
            if arg_buff_equipment_data.get("equipment"):
                for buff_equipment in arg_buff_equipment_data.get("equipment"):
                    setattr(self, f'equipment_{buff_equipment.get("slotId").lower()}', buff_equipment.get('itemName'))
                    if buff_equipment.get("slotId") == 'TITLE':
                        setattr(self, f'equipment_{buff_equipment.get("slotId").lower()}_enchant', explain_enchant(buff_equipment.get('enchant')))
                    else:
                        pass
            else:
                pass
            # 버프 강화 정보
            if arg_buff_equipment_data.get("skillInfo"):
                for index, value in enumerate(arg_buff_equipment_data['skillInfo']['option']['values']):
                    arg_buff_equipment_data['skillInfo']['option']['desc'] = arg_buff_equipment_data['skillInfo']['option']['desc'].replace("{" + f"value{index + 1}" + "}", value)
                self.buff_level = arg_buff_equipment_data['skillInfo']['option']['level']
                self.buff_desc = arg_buff_equipment_data['skillInfo']['option']['desc']              
            
    
        # 버프 강화 아바타
        if arg_buff_avatar_data.get("skill", dict()).get('buff'):
            arg_buff_avatar_data = arg_buff_avatar_data.get("skill", dict()).get('buff')
            if arg_buff_avatar_data.get("avatar"):
                for buff_avatar in arg_buff_avatar_data.get("avatar"):
                    if buff_avatar.get("slotId").lower() in PLATINUM_AVATAR_LIST:
                        # setattr(self, f'avatar_{buff_avatar.get("slotId").lower()}', BuffPlatimun())
                        getattr(self, f'avatar_{buff_avatar.get("slotId").lower()}').get_buff_avatar_data(buff_avatar)
                    else:
                        # setattr(self, f'avatar_{buff_avatar.get("slotId").lower()}', BuffAvatar())
                        getattr(self, f'avatar_{buff_avatar.get("slotId").lower()}').get_buff_avatar_data(buff_avatar)

        # 버프 강화 크리쳐
        if arg_buff_creature_data.get("skill", dict()).get('buff'):
            arg_buff_creature_data = arg_buff_creature_data.get("skill", dict()).get('buff')
            if arg_buff_creature_data.get('creature'):
                for creature in arg_buff_creature_data.get('creature'):
                    setattr(self, 'creature', creature.get('itemName'))

class CharacterFame(PyNeople):
    """
    Neople Open API 16. 캐릭터 명성 검색
    """    

    def __init__(self, arg_api_key: str):
        super().__init__(arg_api_key)

    def get_data(self, arg_min_fame : int, 
                  arg_max_fame : int,
                  arg_job_id : str = "",
                  arg_job_grow_id : str = "",
                  arg_is_all_job_grow : bool = False, 
                  arg_is_buff : bool = "", 
                  arg_server_id : str = "all",
                  arg_limit : int = 200):
        """
        해당 명성 구간의 캐릭터 정보를 원소로 가지는 list를 반환함
            Args : 
                arg_min_fame(int) : 명성 구간 최소값(최대 명성과의 차이가 2000이상이면 최대명성 - 2000 으로 입력됨)
                arg_max_fame(int) : 명성 구간 최대값
                arg_job_id(str) : 캐릭터 직업 고유 코드
                arg_job_grow_id(str) : 캐릭터 전직 직업 고유 코드(jobId 필요)
                arg_is_all_job_grow(bool) : jobGrowId 입력 시 연계되는 전체 전직 포함 조회 ex) 검성 -> 웨펀마스터, 검성, 검신, 眞웨펀마스터
                arg_is_buff(bool) : 버퍼만 조회(true), 딜러만 조회(false), 전체 조회(미 입력)	
                arg_server_id(str) : 서버 아이디
                arg_limit(int) : 반환 Row 수
        """
        url = f"https://api.neople.co.kr/df/servers/{arg_server_id}/characters-fame?minFame={arg_min_fame}&maxFame={arg_max_fame}&jobId={arg_job_id}&jobGrowId={arg_job_grow_id}&isAllJobGrow={arg_is_all_job_grow}&isBuff={arg_is_buff}&limit={arg_limit}&apikey={self._api_key}"
        return get_request(url)
    
    