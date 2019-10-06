#by cuining
#2019.10.5
from removebg import RemoveBg
from PIL import Image

while True:
    chose = input(
        """
        ***************************************
        *          欢迎使用本工具             *
        * 工具是调用www.remove.bg的API实现抠图 *
        *    因此自行前往网站注册申请API密钥    *
        *       个人账户每月免费50张           *
        *=====================================*
        *       去除背景		请按  1           *
        *       退出工具		请按  0           *
        ***************************************        
        """
    )
    if chose == '1':
    	api_key = input("请填入你的API密钥：\n")
    	rmbg = RemoveBg(api_key, "./error.log") # 参数填入 api-key, 错误日志路径
    	image_path0 = input("请输入图片地址（例如：G:/photo）：\n")
    	image_path1 = input("请输入图片名称（例如：img.png）：\n")
    	image_path = image_path0+'/'+image_path1
    	rmbg.remove_background_from_img_file(image_path)
    	print("抠图已完成！")
    	chose = input("""
            **********************************
            *     是否需要更换常用背景颜色？    *
            *           红底   请按 1         *
            *           蓝底   请按 2         *
            *           白底   请按 3         *
            *           不需要 请按 0         *
            **********************************
            """)
    	im = Image.open(image_path0+'/'+image_path1+'_no_bg.png')
    	x, y = im.size
    	print(x,y)
    	if chose == '1':
    		try:
    			p = Image.new('RGBA', im.size, (255, 0, 0))
    			p.paste(im, (0, 0, x, y), im)
    			p.save(image_path0+'/'+image_path1+'_red_bg.png')
    		except:
    			print('error!')
    		exit()
    	elif chose == '2':
    		try:
    			p = Image.new('RGBA', im.size, (0, 0, 255))
    			p.paste(im, (0, 0, x, y), im)
    			p.save(image_path0+'/'+image_path1+'_blue_bg.png')
    		except:
    			print('error!')
    		exit()
    	elif chose == '3':
    		try:
    			p = Image.new('RGBA', im.size, (255, 255, 255))
    			p.paste(im, (0, 0, x, y), im)
    			p.save(image_path0+'/'+image_path1+'_white_bg.png',dpi=(300.0,300.0))
    		except:
    			print('error!')
    		exit()
    	elif chose == '0':
    		print('欢迎下次使用~~~')
    		exit()

    elif chose == '0':
        print("欢迎下次使用~~~")
        break
    else:
        print("输入有误请重新输入~~~")