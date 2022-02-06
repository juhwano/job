from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from users.models import User
from users.models import MiddleCate


# 회원가입
def signup(request):
    print('회원가입화면 호출')

    #중분류 정보 보내기
    middle_cate = MiddleCate.objects.all()
    context={'middle_cate':middle_cate}

    return render(request, 'register.html', context)

# 회원가입 정보 전송
def signup2(request):

    # form 정보 가져오기
    data = request.POST
    useremail = data.get('useremail')
    userpw = data.get('userpw')
    pwverify = data.get('pwverify')
    gender = data.get('gender')
    work_state = data.get('work_state')
    nickname = data.get('nickname')
    age = data.get('age')
    middle_level= data.get("middle_level")
    # error 메세지 담을 dic
    res_data = {}

    # 이메일 중복 체크

    try :
        user_info = User.objects.get(useremail=useremail)

        if user_info:
            res_data['error'] = '사용 불가능한 이메일'
            return render(request, 'register.html', res_data)
    except :

        # 입력 값 중 빈값 체크
        if not (gender and work_state and age and nickname.strip()) :
            res_data['error'] = '모든 값을 입력해야 합니다.'

        # 비밀번호 확인 일치여부 체크
        elif userpw != pwverify :
            res_data['error'] = '비밀번호 확인 불일치'

        # 비밀번호 길이 체크
        elif len(userpw)<8 :
            res_data['error'] = '비밀번호 8자 이상 설정해주세요'

        # db에 저장
        else :
            member=User(useremail=useremail,
                        userpw=userpw,
                        nickname=nickname,
                        age=age,
                        gender=gender,
                        work_state=work_state,
                        join_date=datetime.now(),
                        middle_level = middle_level
                        )
            # db에 전송
            member.save()
            # 전송 후 index 로 redirect
            return redirect('/index')

        # 위의 유효성 검증에서 걸렸을 경우 에러메세지와 함께 랜더링
        return render(request, 'register.html', res_data)

# 로그인
def signin(request):

    # 로그인 화면 호출
    if request.method == 'GET':
        return render(request,'login.html')

    # 로그인 입력값 전송
    elif request.method == 'POST':
        # 전송받은 이메일 비밀번호 확인
        data = request.POST
        useremail = data.get('useremail')
        userpw = data.get('userpw')

        # 오류메세지 담을 dic
        res_data={}

        # 유효성처리
        # 빈값 체크
        if not (useremail and userpw):
            res_data['error']='모든 칸을 다 입력해주세요'
        else :
            # 탈퇴회원 체크 - 로그인 불가능
            user_info = User.objects.get(useremail=useremail)
            print(user_info)
            if user_info.withdrawal == 1 :
                res_data['error'] = '회원이 아닙니다.'
                return render(request, 'login.html', res_data)

            # db에 저장된 id와 pw 가 일치하는지 확인
            if (useremail == user_info.useremail) and (userpw == user_info.userpw) :
                request.session['useremail'] = useremail
                print('useremail session>>' , request.session['useremail'] )
                return redirect('/index')

            # 유효성 검증 실패 - 에러메세지 전달
            else :
                res_data['error'] = '올바른 이메일과 비밀번호를 입력해주세요.'
        return render(request, 'login.html',res_data)


# 로그아웃
def logout(request):
    # 로그아웃은 session에 저장된 user_id값을 지우면 된다.
    if request.session.get('useremail'):
        del(request.session['useremail'])

    # 로그아웃 후 index로 이동
    return redirect('/index')

# 정보(profile) 확인
def userinfo(request,id):
    # 세션 정보 가져오기
    session_id = request.session['useremail']
    user_info = User.objects.get(useremail=session_id)

    # template에 정보 보내기 전에 mapping
    if user_info.gender ==0 :
        gender = '남성'
    else : 
        gender ='여성'
    if user_info.work_state ==0 :
        work_state = '구직'
    else : 
        work_state ='재직'

    # 보낼 정보
    context={'userinfo':user_info,
             'gender':gender,
             'work_state':work_state}
    return render(request, 'userinfo.html',context)

# 수정 화면 호출
def userupdate(request, id):

    #중분류 정보 보내기
    middle_cate = MiddleCate.objects.all()

    # 세션을 통해 정보 가져오기
    session_id = request.session['useremail']
    user_info = User.objects.get(useremail=session_id)

    # age의 경우 jan.1.2022 와 같이 표시 되기 때문에 str로 변경해서 넘겨줌
    context = {'userinfo': user_info,
               'age':str(user_info.age),
               'middle_cate':middle_cate}
    return render(request, 'infoupdate.html', context)

# 정보 수정 전송
def userupdate2(request):

    # 수정된 정보 template에서 가져오기
    data = request.POST

    useremail = data.get('useremail')
    userpw = data.get('userpw')
    pwverify = data.get('pwverify')
    nickname = data.get('nickname')
    age = data.get('age')
    gender = data.get('gender')
    work_state = data.get('work_state')
    middle_level = data.get('middle_level')

    # 세션을 통해서 기존 정보 가져와서 미리 input에 들어가있도록 함
    session_id = request.session['useremail']
    user_info = User.objects.get(useremail=session_id)
    res_data={
        'userinfo':user_info,
        'age': str(user_info.age)
    }

    # 유효성검증
    # 빈값 체크
    if not (gender and work_state and age and nickname.strip()):
        res_data['error'] = '모든 값을 입력해야 합니다.'

    # 비밀번호 재확인 체크
    elif userpw != pwverify:
        res_data['error'] = '비밀번호 확인 불일치'

    # 비밀번호 길이 체크
    elif len(userpw) < 6:
        res_data['error'] = '비밀번호 6자 이상 설정해주세요'


    else:
        # 수정을 할 때는 미리 검색을 한 번 하고,
        member = User.objects.get(useremail=session_id)

        # 해당 컬럼값 변경해주고
        member.useremail = useremail
        member.nickname = nickname
        member.userpw = userpw
        member.age = age
        member.gender = gender
        member.work_state = work_state
        member.middle_level = middle_level

        # 수정된 것 저장.
        member.save()
        return redirect('/index')
    return render(request, 'infoupdate.html', res_data)

# 회원 탈퇴 창 호출
def userdelete(request,id):
    return render(request, 'withdrawal.html')

# 회원탈퇴 정보 전송
def userdelete2(request) :

    # 세션 정보 가져오기
    session_id = request.session['useremail']
    user_info = User.objects.get(useremail=session_id)

    # 비밀번호 입력
    data = request.POST

    # db에 저장된 비밀번호와 일치하면 탈퇴 가능
    if data.get('userpw') == user_info.userpw:

        # 유저 정보 삭제하지 않고 withdrawal에 표기해서 따로 관리
        user_info.withdrawal = 1
        user_info.withdrawal_date = datetime.now()
        user_info.save()
        # 세션 지우기
        del(request.session['useremail'])

        return redirect('/index')

    # 비밀번호 불일치 회원탈퇴 불가능
    else:
        res_data = {'error': '비밀번호가 일치하지 않습니다.'}
        return render(request, 'withdrawal.html', res_data)



