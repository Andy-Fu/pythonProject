import win32api
import win32con
import win32cred

def get_lockscreen_password():
    # 获取锁屏密码
    password = None
    try:
        # 获取默认凭据
        cred = win32cred.CredRead(None, win32cred.CRED_TYPE_GENERIC, 0)
        # 获取密码
        password = win32cred.CredUnPackAuthenticationBuffer(win32cred.CRED_PACK_PROTECTED_CREDENTIALS, cred['CredentialBlob'])[1]
    except Exception as e:
        print("获取锁屏密码失败：", e)
    return password
if __name__ == '__main__':
    get_lockscreen_password()
