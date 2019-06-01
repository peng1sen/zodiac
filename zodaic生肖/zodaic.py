"""
生肖算年紀
鼠、牛、虎、兔、龍、蛇、馬、羊、猴、雞、狗、豬

"""
import datetime
import tkinter as tk


def time_3():
    b =datetime.datetime.now().strftime("%Y")
    return b

def zodaic(animal):
    year_old_list=[]
    list_zodaic ={'鼠':2008,'牛':2009,'虎':2010,'兔':2011,
                  '龍':2012,'蛇':2013,'馬':2014,'羊':2015,
                  '猴':2016,'雞':2017,'狗':2018,'豬':2019}
    year = int(time_3())
#    animal = input('生肖：')
    zodaic = int(list_zodaic['%s'%animal])
    year_old = year-zodaic
    frist_old = year_old#回圈內無法抓到第一個年齡，所以要另外抓取
    while year_old<100:
        year_old = year_old+12
        year_old_list.append(year_old)
    year_old_list.append(frist_old)#!與第一個年齡組合
    year_old_list.sort()#排序
    return year_old_list

##ans = '鼠'
##print(zodaic(ans))
def frame():
    window = tk.Tk()
    window.title('屬什麼生肖是幾歲？')
    window.geometry('250x260')

    frm_title = tk.Frame(window)
    frm = tk.Frame(window)

    frm_title.pack()
    frm.pack()

    frm_title = tk.Frame(frm_title)

    frm_lelf = tk.Frame(frm, )
    frm_right = tk.Frame(frm)
    frm_top = tk.Frame(frm)
    frm_button = tk.Frame(frm)

    frm_title.pack(side='top')
    frm_lelf.pack(side='left')
    frm_right.pack(side='right')
    frm_top.pack(side='top')
    frm_button.pack(side='bottom')

    title_scale = 25
    content_scale =18
    tk.Label(frm_title, text='',font=('Arial',20 )).pack()
    tk.Label(frm_title, text='生肖幾歲?(%s)'%time_3(),font=('Arial',title_scale )).pack()

    var = tk.StringVar()
    l = tk.Label(frm_title, bg='yellow', text='選擇生肖',font=('Arial', 18))
    l.pack()

    tk.Label(window, text='make by eason 2019',font=('Arial', 10)).pack()

    def print_selection():
        l.config(text=var.get()[1]+'可能的是\n' + var.get())

    ans = '鼠'
    r1 = tk.Radiobutton(frm_lelf, text=ans,
                        variable=var, value=(zodaic(ans)),
                        command=print_selection,font=('Arial', content_scale))
    r1.pack()

    ans = '牛'
    r2 = tk.Radiobutton(frm_lelf, text=ans,
                        variable=var, value=(zodaic(ans)),
                        command=print_selection,font=('Arial', content_scale))
    r2.pack()


    ans = '虎'
    r3 = tk.Radiobutton(frm_lelf, text=ans,
                        variable=var, value=(zodaic(ans)),
                        command=print_selection,font=('Arial', content_scale))
    r3.pack()

    ans = '兔'
    r4 = tk.Radiobutton(frm_lelf, text=ans,
                        variable=var, value=(zodaic(ans)),
                        command=print_selection,font=('Arial', content_scale))
    r4.pack()

    ans = '龍'
    r5 = tk.Radiobutton(frm_top, text=ans,
                        variable=var, value=(zodaic(ans)),
                        command=print_selection,font=('Arial', content_scale))
    r5.pack()

    ans = '蛇'
    r6 = tk.Radiobutton(frm_top, text=ans,
                        variable=var, value=(zodaic(ans)),
                        command=print_selection,font=('Arial', content_scale))
    r6.pack()

    ans = '馬'
    r7 = tk.Radiobutton(frm_top, text=ans,
                        variable=var, value=(zodaic(ans)),
                        command=print_selection,font=('Arial', content_scale))
    r7.pack()

    ans = '羊'
    r8 = tk.Radiobutton(frm_top, text=ans,
                        variable=var, value=(zodaic(ans)),
                        command=print_selection,font=('Arial', content_scale))
    r8.pack()

    ans = '猴'
    r9 = tk.Radiobutton(frm_right, text=ans,
                        variable=var, value=(zodaic(ans)),
                        command=print_selection,font=('Arial', content_scale))
    r9.pack()

    ans = '雞'
    r10 = tk.Radiobutton(frm_right, text=ans,
                        variable=var, value=(zodaic(ans)),
                        command=print_selection,font=('Arial', content_scale))
    r10.pack()

    ans = '狗'
    r11 = tk.Radiobutton(frm_right, text=ans,
                        variable=var, value=(zodaic(ans)),
                        command=print_selection,font=('Arial', content_scale))
    r11.pack()

    ans = '豬'
    r12 = tk.Radiobutton(frm_right, text=ans,
                        variable=var, value=(zodaic(ans)),
                        command=print_selection,font=('Arial', content_scale))
    r12.pack()




def main():
    frame()


if __name__ == "__main__":
    main()
