＃-*-编码：UTF-8-*-
＃xizhi撰写

导入 操作系统
导入 时间
尝试：
  来自 pyzbar。pyzbar 导入 解码
除了 ImportError：
  打印（“ pyzbar模块没有安装好哦\ n 5秒后自动退出”）
  时间。睡觉（5）
  os。_退出（0）
尝试：
  从 PIL 导入 图片
除了 ImportError：
  打印（“ pyzbar模块的依赖库pillow没有安装好哦\ n 5秒后自动退出”）
  时间。睡觉（5）
  os。_退出（0）

打印（“ \ n请复制粘贴二维码的图片路径（含后缀）或拖拽二维码的图片到该窗口” \
      “ \ n如果不想每次都输入路径请将二维码的图片移动到该目录下，然后名字强制改为q.png，名字需要完全一样，直接按确定即可” \
      “ \ n如果一个图片包含多个二维码的会批量解析完”）
qrdecodeimg  =  input（“支持常见的图片后缀（gif，png，jpg等）：”）。replace（“ \” “，”“）。replace（” \' “，”“）
如果 qrdecodeimg  ==  “”：
  qrdecodeimg  =  “ q.png”
尝试：
  图片。打开（qrdecodeimg）。转换（“ RGBA”）。保存（qrdecodeimg）
  qrdecodel  = []
  qrdecode  = 解码（图片。打开（qrdecodeimg））
  对于 内容 中 qrdecode：
    qrdecodel。append（内容。数据。解码（“ utf-8”））
  qrdecode  =  “ \ n ”。加入（qrdecodel）
  打印（“ \ n解码内容为：\ n \ n％s \ n \ n将以上内容分别复制到需要的地方即可，程序30秒后自动退出” ％（qrdecode））
  时间。睡觉（30）
  os。_退出（0）
除了 FileNotFoundError：
  打印（“ \ n该目录下没有％s文件哦\ n 5秒后自动退出” ％（qrdecodeimg））
  时间。睡觉（5）
  os。_退出（0）
