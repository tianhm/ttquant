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

#运行系统环境设置
#G_os=1 windows,=2 linux, =3 mac oS
global G_os   #操作系统
global G_pyver  #Python版本
global G_tk  #tkinter命令
global G_tk1 #tkinter命令
global G_tk2 #tkinter命令
global G_py2 #python2命令
global G_py3 #python3命令

#软件环境设置
global G_name  #软件名称
global G_title #软件标题
global G_winW  #默认主窗口宽度
global G_winH  #默认主窗口高度
global G_ver   #软件版本号
global G_user  #用户名
global G_ico   #软件图标
global G_login  #用户登录标记
global G_root   #窗口根句柄
global G_canvas  #绘图canvas
global G_figure  #绘图figure
global G_plot    #绘图plot
global tk    #tk
global ttk   #ttk


###########################################
#软件参数
global G_gtype   #画面模式,暂用于显示指标图形个数
global G_stock   #当前股票代码
global G_index   #当前用户指标
global G_df      #当前股票代码数据
global G_sday    #分析开始日期
global G_eday    #分析结束日期
global G_MA1     #价格平均线周期
global G_MA2     #价格平均线周期
global G_MA3     #价格平均线周期
global G_MA4     #价格平均线周期
global G_MA5     #价格平均线周期
global G_MA6     #价格平均线周期
global G_MAV1     #成交量平均线周期
global G_MAV2     #成交量平均线周期

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