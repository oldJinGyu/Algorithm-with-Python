import pyautogui
#장바구니 조회(280,445)
#식건(388,402)
#컴네(380,354)
#창프입(398,418)
#확인(1109, 158)
while True:
    pyautogui.click(x=280, y=445)

# pyautogui.moveTo(380, 354) #컴네누르기
    pyautogui.click(x=380, y=354)
# pyautogui.moveTo(1109, 158) #확인 누르기
# pyautogui.click()

    # pyautogui.moveTo(388, 410) #식건누르기
    pyautogui.click(x=388,y=410)
# pyautogui.moveTo(1109, 158) #확인 누르기
# pyautogui.click()

    # pyautogui.moveTo(398, 415) #창프입 누르기
    pyautogui.click(x=398,y=415)
# pyautogui.moveTo(1109, 158) #확인 누르기
    pyautogui.click(x=1109, y=158)