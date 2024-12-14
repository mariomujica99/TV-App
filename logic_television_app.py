from PyQt6.QtWidgets import *
from gui_television_app import *

class Logic(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 0
    MAX_CHANNEL = 9

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__status = False
        self.__muted = False
        self.__volume = Logic.MIN_VOLUME
        self.__channel = Logic.MIN_CHANNEL
        self.slider_volume.setMinimum(Logic.MIN_VOLUME)
        self.slider_volume.setMaximum(Logic.MAX_VOLUME)
        self.slider_volume.setValue(Logic.MIN_VOLUME)

        self.button_0.clicked.connect(lambda: self.channel_buttons())
        self.button_1.clicked.connect(lambda: self.channel_buttons())
        self.button_2.clicked.connect(lambda: self.channel_buttons())
        self.button_3.clicked.connect(lambda: self.channel_buttons())
        self.button_4.clicked.connect(lambda: self.channel_buttons())
        self.button_5.clicked.connect(lambda: self.channel_buttons())
        self.button_6.clicked.connect(lambda: self.channel_buttons())
        self.button_7.clicked.connect(lambda: self.channel_buttons())
        self.button_8.clicked.connect(lambda: self.channel_buttons())
        self.button_9.clicked.connect(lambda: self.channel_buttons())

        self.button_power.clicked.connect(lambda: self.power())
        self.button_mute.clicked.connect(lambda: self.mute())
        self.button_plus.clicked.connect(lambda: self.volume_up())
        self.button_minus.clicked.connect(lambda: self.volume_down())
        self.button_up.clicked.connect(lambda: self.channel_up())
        self.button_down.clicked.connect(lambda: self.channel_down())


    def power(self):
        if self.__status:
            self.__status = False
            self.label_channel.setText(f'Power Off')
            self.label_screen.setPixmap(QtGui.QPixmap("black.jpg"))
        else:
            self.__status = True
            self.label_channel.setText(f'Power On')
            self.label_screen.setPixmap(QtGui.QPixmap("hello.jpg"))

    def mute(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
                self.slider_volume.setValue(self.__volume)
                self.label_volume.setText(f'{self.__volume}')
            else:
                self.__previous_volume = self.__volume
                self.__muted = True
                self.__volume = Logic.MIN_VOLUME
                self.slider_volume.setValue(self.__volume)
                self.label_volume.setText(f'{self.__volume}')
            return self.__muted

    def channel_up(self):
        if self.__status:
            if self.__channel == Logic.MAX_CHANNEL:
                self.__channel = Logic.MIN_CHANNEL
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()
            else:
                self.__channel += 1
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()

    def channel_down(self):
        if self.__status:
            if self.__channel == Logic.MIN_CHANNEL:
                self.__channel = Logic.MAX_CHANNEL
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()
            else:
                self.__channel -= 1
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()

    def channel_buttons(self):
        if self.__status:
            sender = self.sender()
            if sender == self.button_0:
                self.__channel = 0
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()
            elif sender == self.button_1:
                self.__channel = 1
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()
            elif sender == self.button_2:
                self.__channel = 2
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()
            elif sender == self.button_3:
                self.__channel = 3
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()
            elif sender == self.button_4:
                self.__channel = 4
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()
            elif sender == self.button_5:
                self.__channel = 5
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()
            elif sender == self.button_6:
                self.__channel = 6
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()
            elif sender == self.button_7:
                self.__channel = 7
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()
            elif sender == self.button_8:
                self.__channel = 8
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()
            elif sender == self.button_9:
                self.__channel = 9
                self.label_channel.setText(f'Channel {self.__channel}')
                self.tv_screen()

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume == Logic.MAX_VOLUME:
                self.__volume = Logic.MAX_VOLUME
                self.slider_volume.setValue(self.__volume)
                self.label_volume.setText(f'{self.__volume}')
            else:
                self.__volume += 1
                self.slider_volume.setValue(self.__volume)
                self.label_volume.setText(f'{self.__volume}')

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume == Logic.MIN_VOLUME:
                self.__volume = Logic.MIN_VOLUME
                self.slider_volume.setValue(self.__volume)
                self.label_volume.setText(f'{self.__volume}')
            else:
                self.__volume -= 1
                self.slider_volume.setValue(self.__volume)
                self.label_volume.setText(f'{self.__volume}')

    def tv_screen(self):
        if self.__status:
            if self.__channel == 0:
                self.label_screen.setPixmap(QtGui.QPixmap("hgtv.jpg"))
            elif self.__channel == 1:
                self.label_screen.setPixmap(QtGui.QPixmap("espn.jpg"))
            elif self.__channel == 2:
                self.label_screen.setPixmap(QtGui.QPixmap("cw.jpg"))
            elif self.__channel == 3:
                self.label_screen.setPixmap(QtGui.QPixmap("cn.jpg"))
            elif self.__channel == 4:
                self.label_screen.setPixmap(QtGui.QPixmap("pbs.jpg"))
            elif self.__channel == 5:
                self.label_screen.setPixmap(QtGui.QPixmap("history.jpg"))
            elif self.__channel == 6:
                self.label_screen.setPixmap(QtGui.QPixmap("hallmark.jpg"))
            elif self.__channel == 7:
                self.label_screen.setPixmap(QtGui.QPixmap("nickelodeon.jpg"))
            elif self.__channel == 8:
                self.label_screen.setPixmap(QtGui.QPixmap("abc.jpg"))
            elif self.__channel == 9:
                self.label_screen.setPixmap(QtGui.QPixmap("ngc.jpg"))

    def __str__(self):
        return (f'Power = {self.__status}, '
                f'Channel = {self.__channel}, '
                f'Volume = {self.__volume}')