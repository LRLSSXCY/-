
#  导入工具函数包
import cards_tools
while True:
    cards_tools.show_menu()
    action_str = input("请选择您希望执行的操作：")
    print("您选择的操作是 [%s]" % action_str)
    # 1,2,3 针对系统的操作
    if action_str in ["1", "2", "3"]:

        if action_str == "1":
            cards_tools.new_card()

        elif action_str == "2":
            cards_tools.show_all()

        elif action_str == "3":
            cards_tools.search_card()

    # 0 退出系统
    elif action_str == "0":
        print("成功退出，欢迎再次使用 ")
        break
    else:
        print("您输入的不正确，请重新选择")
