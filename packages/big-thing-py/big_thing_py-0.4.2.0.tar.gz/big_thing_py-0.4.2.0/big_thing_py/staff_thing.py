from big_thing_py.core.thing import *


class MXStaffThing(MXThing, metaclass=ABCMeta):

    def __init__(
        self,
        name: str,
        category: MXDeviceCategory,
        desc: str,
        version: str,
        service_list: List[MXService],
        alive_cycle: float,
        is_parallel: bool,
        is_matter: bool,
        staff_thing_id: str = None,
    ):
        super().__init__(
            name=name,
            desc=desc,
            category=category,
            version=version,
            service_list=service_list,
            alive_cycle=alive_cycle,
            is_super=False,
            is_parallel=is_parallel,
            is_builtin=False,
            is_manager=False,
            is_matter=is_matter,
        )
        self._staff_thing_id = staff_thing_id
        self._is_alive = False

    def __eq__(self, o: 'MXStaffThing') -> bool:
        instance_check = isinstance(o, MXStaffThing)
        staff_thing_id_check = o._staff_thing_id == self._staff_thing_id

        # return super().__eq__(o) and instance_check and staff_thing_id_check
        return instance_check and staff_thing_id_check

    def add_staff_service(self, service_list: List[MXService]) -> None:
        for staff_service in service_list:
            self.add_service(staff_service)

    @abstractmethod
    def setup_service_list(self) -> None:
        pass

    @abstractmethod
    async def setup(self) -> bool:
        pass

    @abstractmethod
    async def wrapup(self) -> bool:
        pass

    # ====================================
    #               _    _
    #              | |  | |
    #   __ _   ___ | |_ | |_   ___  _ __
    #  / _` | / _ \| __|| __| / _ \| '__|
    # | (_| ||  __/| |_ | |_ |  __/| |
    #  \__, | \___| \__| \__| \___||_|
    #   __/ |
    #  |___/
    # ====================================

    @property
    def staff_thing_id(self) -> str:
        return self._staff_thing_id

    @property
    def is_alive(self) -> bool:
        return self._is_alive

    # ==================================
    #             _    _
    #            | |  | |
    #  ___   ___ | |_ | |_   ___  _ __
    # / __| / _ \| __|| __| / _ \| '__|
    # \__ \|  __/| |_ | |_ |  __/| |
    # |___/ \___| \__| \__| \___||_|
    # ==================================

    @staff_thing_id.setter
    def staff_thing_id(self, id: str) -> None:
        self._staff_thing_id = id

    @is_alive.setter
    def is_alive(self, is_alive: bool) -> None:
        self._is_alive = is_alive
