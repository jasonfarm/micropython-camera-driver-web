import camera
import network

def connect_wifi():
    try:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to wifi...')
            wlan.connect('HW-TT', '88643119')

            while not wlan.isconnected():
                pass
        ifconfig = wlan.ifconfig()
        print('网路配置', ifconfig)
        return ifconfig[0]

    except:
        print('网路配置异常')
        return ""

def camera_init():
    print('camera_init')
    # 摄像头初始化
    try:
        if not camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM):
            print("camera.init False")
    except Exception as e:
        camera.deinit()
        if not camera.init(0, format=camera.JPEG):
            print("camera.init False")
            return

    # 其他设置
    # 上下翻转
    camera.flip(1)
    # 左/右
    camera.mirror(1)
    # 分辨率
    camera.framesize(camera.FRAME_VGA)
    # 选项如下
    # FRAME_96x96 FRAME_QQVGA FRAME_QCIF  FRAME_HQVGA FRAME_240x240
    # FRAME_QVGA  FRAME_CIF   FRAME_HVGA  FRAME_VGA   FRAME_SVGA
    # FRAME_XGA   FRAME_HD    FRAME_SXGA  FRAME_UXGA  FRAME_FHD
    # FRAME_P_HD  FRAME_P_3MP FRAME_QXGA  FRAME_QHD   FRAME_WQXGA
    # FRAME_P_FHD FRAME_QSXGA
    # FRAME_96x96: 96x96 像素
    # FRAME_QQVGA: 160x120 像素（可能是 QQVGA，一个非常低的分辨率）
    # FRAME_QCIF: 176x144 像素
    # FRAME_HQVGA: 240x160 像素（比 QVGA 高）
    # FRAME_240x240: 240x240 像素（正方形）
    # FRAME_QVGA: 320x240 像素
    # FRAME_CIF: 352x288 像素（常用于视频会议）
    # FRAME_HVGA: 480x320 像素
    # FRAME_VGA: 640x480 像素
    # FRAME_SVGA: 800x600 像素
    # FRAME_XGA: 1024x768 像素
    # FRAME_HD: 1280x720 像素（高清）
    # FRAME_SXGA: 1280x1024 像素
    # FRAME_UXGA: 1600x1200 像素
    # FRAME_FHD: 1920x1080 像素（全高清）
    # FRAME_P_HD: 1280x720 像素，逐行扫描（可能是 "P" 代表 "Progressive"）
    # FRAME_P_3MP: 2048x1536 像素（3百万像素）
    # FRAME_QXGA: 2048x1536 像素
    # FRAME_QHD: 2560x1440 像素（四倍高清）
    # FRAME_WQXGA: 2560x2048 像素
    # FRAME_P_FHD: 1920x1080 像素，逐行扫描
    # FRAME_QSXGA: 2560x2048 像素
    # 有关详细信息，请查看连接 https://bit.ly/qYOzizz

    # 特效
    camera.speffect(camera.EFFECT_NONE)
    # 选项如下：
    # 效果\无（默认）效果\负效果\Bw效果\红色效果\绿色效果\蓝色效果\复古效果
    # EFFECT_ NONE (default) EFFECT_NEG \EFFECT_BW\ EFFECT_RED\ EFFECT_GREEN\ EFFECT_BLUE\ EFFECT_RETRO

    # 白平衡
    camera.whitebalance(camera.WB_HOME)
    #选项如下:
    # WB_NONE (default) WB_SUNNY WB_CLOUDY WB_OFFICE WB_HOME

    # 饱和度
    camera.saturation(0)
    # -2, 2 (默认0) -2 灰度

    # 亮度
    camera.brightness(0)
    # -2, 2 (默认0）亮度

    # 对比度
    camera.contrast(0)
    # -2,2 (默认0）2高对比度

    # 质量
    camera.quality(10)
    #10-63 数值越小质量越高

    camera.rawgma(1)

def run():
    import time
    from machine import Pin
    camera_init()
    ip = connect_wifi()
    print("Camera Ready! Use 'http://"+ip + "'to connect" )
    #camera.start_camera_server_car(1, wifi_addr=ip)
    camera.start_camera_server_car(1, wifi_addr=ip, qplb=12, qplf=13, qprb=14, qprf=15, led=4)
    led = Pin(4, Pin.OUT)
    for i in range(3):
        led.value(1)
        time.sleep(0.1)
        led.value(0)
        time.sleep(0.5)


if __name__ == "__main__":
    run()
