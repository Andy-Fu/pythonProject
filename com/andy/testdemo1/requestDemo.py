import requests
import json

url = "https://wx.mail.qq.com/info/report?sid=zT42RoyyUXkukTN1AFU2SQAA&r=31894749668331672328492409&sid=gL68R-VBJ7YbB1Ix"
data = {
    "sid":"zT42RoyyUXkukTN1AFU2SQAA",
    "r":"31894749668331672328492409",
    "sid":"gL68R-VBJ7YbB1Ix"

}
def cookie_demo():
    headers = {
        "Cookie":"RK=f4nxAMTBZJ; ptcz=ef8f105802854ece0aa7982a1772971fd48c794b109e827615553343cd9446d5; webp=1; pgv_pvid=3863930250; fqm_pvqid=27b771f6-f193-4055-b5db-12a90775614b; pac_uid=0_434dbf7afaea7; tvfe_boss_uuid=76e5d39c2e691afe; o_cookie=1435611710; _clck=q1vhhk|1|f4x|0; qm_device_id=KaXIoSKnrEgl0dkT2iP1CGVrtbMgQWJSb7t+QUSoPE3UbLnitnQhEpuG2EsmX7DQ; edition=mail.qq.com; qm_logintype=qq; CCSHOW=000001; lang=zh-CN; ptui_loginuin=1435611710; uin=o1435611710; skey=@0YZfAK0y8; p_uin=o1435611710; pt4_token=knSNJX4MSAz74ZL8xpTCSq8ARmx3UC4B3uCdwHZHfPA_; p_skey=nBdeDYZzFA9J0MyYWZrYAw-oLR*WAhWTZ853XHP3tu8_; xm_envid=456_hw7ZgpDWoxjbJGypSGPY0oMNQj+cgU9wM0dFNkwjwg44R5ZCLQmVBlZ+m8BmfZ/NSQClFi+pUlsC15K4i0V1OlBU0CbeUreGShkRpNpaCbT1EotbwURoO4OoEnelY3pEh6sJz9YcpUSN+Xx2V9zGsmoM30yKVngelq+DKQ==; qm_username=1435611710; qm_domain=https://mail.qq.com; ssl_edition=sail.qq.com; username=1435611710&1435611710; sid=1435611710&408a19233e22347a29d405ae57aca2b3,qbkJkZURZWnpGQTlKME15WVdacllBdy1vTFIqV0FoV1RaODUzWEhQM3R1OF8.; qm_muti_sid=13102662460486206&gL68R-VBJ7YbB1Ix; xm_uin=13102662460486206; xm_sid=zT42RoyyUXkukTN1AFU2SQAA; xm_muti_sid=13102662460486206&zT42RoyyUXkukTN1AFU2SQAA; xm_skey=13102662460486206&39b3399fcd399681a0abc1ff10a8ec55; xm_ws=13102662460486206&283823d13853879fe6703942c5c5de9e; xm_data_ticket=13102662460486206&CAESIGOttAIALozNVZGyPvBZD6aqwe0FE7yH7uz0A-EEHXNA; new_mail_num=1435611710&0"
    }
    cookies = r"RK=f4nxAMTBZJ; ptcz=ef8f105802854ece0aa7982a1772971fd48c794b109e827615553343cd9446d5; webp=1; pgv_pvid=3863930250; fqm_pvqid=27b771f6-f193-4055-b5db-12a90775614b; pac_uid=0_434dbf7afaea7; tvfe_boss_uuid=76e5d39c2e691afe; o_cookie=1435611710; _clck=q1vhhk|1|f4x|0; qm_device_id=KaXIoSKnrEgl0dkT2iP1CGVrtbMgQWJSb7t+QUSoPE3UbLnitnQhEpuG2EsmX7DQ; edition=mail.qq.com; qm_logintype=qq; CCSHOW=000001; lang=zh-CN; ptui_loginuin=1435611710; uin=o1435611710; skey=@0YZfAK0y8; p_uin=o1435611710; pt4_token=knSNJX4MSAz74ZL8xpTCSq8ARmx3UC4B3uCdwHZHfPA_; p_skey=nBdeDYZzFA9J0MyYWZrYAw-oLR*WAhWTZ853XHP3tu8_; xm_envid=456_hw7ZgpDWoxjbJGypSGPY0oMNQj+cgU9wM0dFNkwjwg44R5ZCLQmVBlZ+m8BmfZ/NSQClFi+pUlsC15K4i0V1OlBU0CbeUreGShkRpNpaCbT1EotbwURoO4OoEnelY3pEh6sJz9YcpUSN+Xx2V9zGsmoM30yKVngelq+DKQ==; qm_username=1435611710; qm_domain=https://mail.qq.com; ssl_edition=sail.qq.com; username=1435611710&1435611710; sid=1435611710&408a19233e22347a29d405ae57aca2b3,qbkJkZURZWnpGQTlKME15WVdacllBdy1vTFIqV0FoV1RaODUzWEhQM3R1OF8.; qm_muti_sid=13102662460486206&gL68R-VBJ7YbB1Ix; xm_uin=13102662460486206; xm_sid=zT42RoyyUXkukTN1AFU2SQAA; xm_muti_sid=13102662460486206&zT42RoyyUXkukTN1AFU2SQAA; xm_skey=13102662460486206&39b3399fcd399681a0abc1ff10a8ec55; xm_ws=13102662460486206&283823d13853879fe6703942c5c5de9e; xm_data_ticket=13102662460486206&CAESIGOttAIALozNVZGyPvBZD6aqwe0FE7yH7uz0A-EEHXNA; new_mail_num=1435611710&0"
    print(json.dumps(cookies))
    response = requests.post(url,headers=headers)
    print(response.text)
    cookie = response.cookies.get_dict()
if __name__ == '__main__':
    cookie_demo()