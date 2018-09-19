# -*- coding: utf-8 -*-
"""
#功能：通通量化投资开发环境全局变量
#版本：Ver1.00
#设计人：独狼荷蒲
#电话:18578755056
#QQ：2775205
#百度：荷蒲指标
#开始设计日期: 2018-07-08
#公众号:独狼股票分析
#使用者请同意最后<版权声明>
#最后修改日期:2018年9月14日
#主程序：HP_main.py
"""

import platform
from HP_global import *
import pandas as pd

# 软件名称
G_root = None
G_name = '通通证券分析研究平台'
G_title = '通通证券分析研究平台'
G_ico = '.\omr.ico'
G_winW = 1280
G_winH = 850
G_ver = 1.00
G_user = '13311968726'
G_passwd = 'ftp123'
G_login = False
G_tk = 'import tkinter as tk'
G_tk1 = 'from tkinter import *'
G_tk2 = 'from tkinter import ttk'
G_os = 1

G_pyver = int(platform.python_version()[0:1])

###########################################
# 软件参数
G_gtype = 3
G_stock = '000001.XSHE'
G_df = None
G_sday = '2018-01-01'
G_eday = '2018-09-08'
G_index = 'KDJ'
G_MA1 = 5
G_MA2 = 10
G_MA3 = 20
G_MA4 = 60
G_MA5 = 120
G_MA6 = 240
G_MAV1 = 5
G_MAV2 = 10


########################################
# 操作系统类型
def UseOS():
    sysstr = platform.system()
    if (sysstr == "Windows" or sysstr == "windows"):
        return 1
    elif (sysstr == "Linux"):
        return 2
    else:
        return 3


def HP_init():
    # 软件名称
    G_name = '聚宽证券分析研究平台'
    G_title = '聚宽证券分析研究平台'
    G_ver = 1.00
    G_login = False
    G_tk = 'import tkinter as tk'
    G_tk1 = 'from tkinter import *'
    G_tk2 = 'from tkinter import ttk'
    G_pyver = int(platform.python_version()[0:1])
    G_os = UseOS()
    if G_pyver == 3:
        G_tk = 'import tkinter as tk'
        G_tk1 = 'from tkinter import *'
        G_tk2 = 'from tkinter import ttk'
    else:
        G_tk = 'import Tkinter as tk'
        G_tk1 = 'from Tkinter import *'
        G_tk2 = 'from Tkinter import ttk'


# 通用平均线计算
def G_MA(Series, n):
    G_pyver = int(platform.python_version()[0:1])
    G_ma = None
    if G_pyver == 2:
        G_MAstr = 'pd.rolling_mean(Series,n)'
        G_ma = eval(G_MAstr)
    else:
        G_MAstr = 'Series.rolling(window=n,center=False).mean()'
        G_ma = eval(G_MAstr)
    return G_ma


#####################################################
################独狼荷蒲软件版权声明###################
'''
独狼荷蒲软件(或通通软件)版权声明
1、独狼荷蒲软件(或通通软件)均为软件作者设计,或开源软件改进而来，仅供学习和研究使用，不得用于任何商业用途。
2、用户必须明白，请用户在使用前必须详细阅读并遵守软件作者的“使用许可协议”。
3、作者不承担用户因使用这些软件对自己和他人造成任何形式的损失或伤害。
4、作者拥有核心算法的版权，未经明确许可，任何人不得非法复制；不得盗版。作者对其自行开发的或和他人共同开发的所有内容，
    包括设计、布局结构、服务等拥有全部知识产权。没有作者的明确许可，任何人不得作全部或部分复制或仿造。

独狼荷蒲软件
QQ: 2775205
Tel: 18578755056
公众号:独狼股票分析
'''
