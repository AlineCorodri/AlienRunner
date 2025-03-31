from background import Background
from const import WIN_WIDTH


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
