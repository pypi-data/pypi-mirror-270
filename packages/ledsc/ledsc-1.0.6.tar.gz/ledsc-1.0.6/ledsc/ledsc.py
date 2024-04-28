import logging
from enum import Enum
from typing import List, Callable

from pymodbus.client import ModbusSerialClient
from pymodbus.pdu import ModbusResponse


class REG(Enum):
    LED_R = 0
    LED_G = 1
    LED_B = 2
    LED_W = 3
    TRANSITION_PER = 4
    LED_LIVE = 5
    PWM_CYCLE = 6
    PX_COUNTER = 7
    PX_TRIGGER = 8

    RESET = 100  # restart driver

    EE_MBADDR = 1000  # Modbus slave address
    EE_SBAUD = 1001  # Serial baud rate
    EE_SPAR = 1002  # Serial Parity (0=NONE, 2=EVEN, 3=ODD)
    EE_LCH_R = 1003  # LED controller channel R
    EE_LCH_G = 1004  # LED controller channel G
    EE_LCH_B = 1005  # LED controller channel B
    EE_LCH_W = 1006  # LED controller channel W
    EE_LDF_TR = 1007  # LED controller default transition time
    EE_LDF_R = 1008  # LED controller default color R
    EE_LDF_G = 1009  # LED controller default color G
    EE_LDF_B = 1010  # LED controller default color B
    EE_LDF_W = 1011  # LED controller default color W
    EE_GR = 1012  # Greeting enable
    EE_PXEN = 1013  # proximity sensor enable
    EE_PWMC = 1014  # PWM cycle
    EE_LOS = 1015  # Light on start


class LedSC:
    def __init__(self, modbus_client: ModbusSerialClient, slave_id: int):
        self.client = modbus_client
        self.slave_id = slave_id
        if self.slave_id == 0:
            logging.warning(f"Using BROADCAST mode!")
        self.write_register = self.__write(self.write_register)
        self.write_registers = self.__write(self.write_registers)

    def __response_check(self, resp):
        if self.slave_id != 0 and issubclass(type(resp), Exception):
            raise resp

    def read_register(self, address: int, count: int = 1):
        """
        :param count: number of bytes to read
        :param address: address to read
        """
        if self.slave_id == 0:
            raise ValueError(f"Reading values is not available in BROADCAST mode!")

        resp = self.client.read_holding_registers(address=address, slave=self.slave_id, count=count)
        self.__response_check(resp)
        resp = resp.registers[0] if len(resp.registers) == 1 else resp.registers
        return resp

    def __write(self, func):
        def wrapper(*args, **kwargs):
            is_broadcast = self.slave_id == 0
            if is_broadcast:
                timeout = self.client.comm_params.timeout_connect
                self.client.close()
                self.client.comm_params.timeout_connect = 0.000001

            resp = func(*args, **kwargs)

            if is_broadcast:
                self.client.comm_params.timeout_connect = timeout  # noqa
            self.__response_check(resp)
        return wrapper

    def write_register(self, address: int, value: int) -> ModbusResponse:
        """
        :param address: Modbus register address
        :param value: value to write
        """
        logging.debug(f"LedController: Writing register ({self.slave_id}): {address}={value}")
        return self.client.write_register(address=address, slave=self.slave_id, value=value)

    def write_registers(self, address: int, values: List[int]) -> ModbusResponse:
        """
        :param address: Modbus register address
        :param values: values to write
        """
        logging.debug(f"LedController: Writing registers ({self.slave_id}): {address}={values}")
        return self.client.write_registers(address=address, slave=self.slave_id, values=values)

    def set_red(self, value: int):
        self.write_register(REG.LED_R.value, value)

    def set_green(self, value: int):
        self.write_register(REG.LED_G.value, value)

    def set_blue(self, value: int):
        self.write_register(REG.LED_B.value, value)

    def set_white(self, value: int):
        self.write_register(REG.LED_W.value, value)

    def set_rgb(self, red: int, green: int, blue: int):
        self.write_registers(REG.LED_R.value, [red, green, blue])

    def set_rgbw(self, red: int, green: int, blue: int, white: int):
        self.write_registers(REG.LED_R.value, [red, green, blue, white])

    def set_live_mode(self, value: bool):
        self.write_register(REG.LED_LIVE.value, 1 if value else 0)

    def get_rgbw(self) -> List[int]:
        return self.read_register(REG.LED_R.value, count=4)

    def get_rgb(self) -> List[int]:
        return self.read_register(REG.LED_R.value, count=3)

    def get_red(self) -> int:
        return self.read_register(REG.LED_R.value)

    def get_live_mode(self) -> int:
        return self.read_register(REG.LED_LIVE.value)

    def get_green(self) -> int:
        return self.read_register(REG.LED_G.value)

    def get_blue(self) -> int:
        return self.read_register(REG.LED_B.value)

    def get_white(self) -> int:
        return self.read_register(REG.LED_W.value)

    def set_transition_time(self, value: float):
        """
        :param value: Transition time in seconds
        """
        self.write_register(REG.TRANSITION_PER.value, round(value*1000))

    def set_pwm_cycle(self, value: int):
        self.write_register(REG.PWM_CYCLE.value, value)

    def set_px_counter(self, value: int):
        self.write_register(REG.PX_COUNTER.value, value)

    def do_px_trigger(self):
        self.write_register(REG.PX_TRIGGER.value, 1)

    def do_reset(self):
        self.write_register(REG.RESET.value, 1)

    def get_transition_time(self) -> int:
        return self.read_register(REG.TRANSITION_PER.value)

    def get_pwm_cycle(self) -> int:
        return self.read_register(REG.PWM_CYCLE.value)

    def get_px_counter(self) -> int:
        return self.read_register(REG.PX_COUNTER.value)

    def set_mb_slave_id(self, value: int):
        self.write_register(REG.EE_MBADDR.value, value)

    def set_serial_baudrate(self, value: int):
        self.write_register(REG.EE_SBAUD.value, value)

    def set_serial_parity(self, value: int):
        self.write_register(REG.EE_SPAR.value, value)

    def set_channel_configuration(self, red: int, green: int, blue: int, white: int):
        self.write_registers(REG.EE_LCH_R.value, [red, green, blue, white])

    def set_greeting_enable(self, value: bool):
        self.write_register(REG.EE_GR.value, value)

    def set_px_enable(self, value: bool):
        self.write_register(REG.EE_PXEN.value, value)

    def set_default_pwm_cycle(self, value: int):
        self.write_register(REG.EE_PWMC.value, value)

    def set_default_rgbw(self, red: int, green: int, blue: int, white: int):
        self.write_registers(REG.EE_LDF_R.value, [red, green, blue, white])

    def set_default_transition_time(self, value: int):
        self.write_register(REG.EE_LDF_TR.value, value)

    def set_light_on_start(self, value: int):
        self.write_register(REG.EE_LOS.value, value)

    def get_mb_slave_id(self) -> int:
        return self.read_register(REG.EE_MBADDR.value)

    def get_serial_baudrate(self) -> int:
        return self.read_register(REG.EE_SBAUD.value)

    def get_serial_parity(self) -> int:
        return self.read_register(REG.EE_SPAR.value)

    def get_channel_configuration(self) -> List[int]:
        return self.read_register(REG.EE_LCH_R.value, count=4)

    def get_greeting_enable(self) -> bool:
        return bool(self.read_register(REG.EE_GR.value))

    def get_px_enable(self) -> bool:
        return bool(self.read_register(REG.EE_PXEN.value))

    def get_default_pwm_cycle(self) -> int:
        return self.read_register(REG.EE_PWMC.value)

    def get_default_rgbw(self) -> List[int]:
        return self.read_register(REG.EE_LDF_R.value, count=4)

    def get_default_transition_time(self) -> int:
        return self.read_register(REG.EE_LDF_TR.value)

    def get_light_on_start(self) -> int:
        return self.read_register(REG.EE_LOS.value)
