//var session_id = '';
// 登录
$(".login").click(function() {
	var email = $(".email").val();
	var password = $(".password").val();
	if (email == '') {
		alert('email is empty');
		return;
	} else if (password == '') {
		alert('password is empty');
		return;
	}

	$.ajax({
		url : 'http://120.27.44.110:5011/mobile/login',
		type : 'GET',
		data : {
			email : email,
			pwd : password,
		},
		dataType : 'json',
		success : function(data) {
			if (data['ret'] == 0) {
				localStorage.email = email;
				login_success(data);
			} else {
				alert('longin failed');
			}
		},
		error : function(e) {
			alert("something is wrong!");
		}
	});
});

function login_success(data) {
	session_id = data['data']['session_id'];
	nickname = data['data']['nickname'];
	localStorage.session_id=session_id;
	localStorage.nickname = nickname;
	$.mobile.changePage("test.html#ireads", {
		transition : "slideup"
	});
}


// 注册
$(".register").click(function() {
	var nickname = $(".nickname").val();
	var email = $(".register_email").val();
	var password = $(".register_password").val();

	if (nickname == '') {
		alert('nickname is empty');
		return;
	} else if (email == '') {
		alert('email is empty');
		return;
	} else if (password == '') {
		alert('password is empty');
		return;
	}

	$.ajax({
		url : 'http://120.27.44.110:5011/mobile/register',
		type : 'GET',
		data : {
			nickname : nickname,
			email : email,
			pwd : password,
		},
		dataType : 'json',
		success : function(data) {
			if (data['ret'] == 0) {
				register_success(data);
			} else if (data['ret'] == 1) {
				alert(data['msg']);
			} else {
				alert('register is failed!');
			}
		},
		error : function(e) {
			alert("something is wrong!");
		}
	});

});

function register_success(data) {
	alert('register success!');
	$.mobile.changePage("test.html#login", {
		transition : "slideup"
	});
}

// 添加关键字
$(".newsubmit").click(function() {
	var keyword = $(".newkeyword").val();
	if (keyword == '') {
		alert('keyword is empty');
		return;
	}
    var session_id = localStorage.session_id;
	$.ajax({
		url : 'http://120.27.44.110:5011/mobile/key_word/add',
		type : 'GET',
		data : {
			session_id : session_id,
			kw : keyword,
			type : 'url',
			create_time : ''
		},
		dataType : 'json',
		success : function(data) {
			if (data['ret'] == 0) {
				add_keyword_success(data);
			} else if (data['ret'] == 1) {
				//alert(data['msg']);
				alert('msg');
			} else {
				alert('Add is failed!');
			}
		},
		error : function(e) {
			alert("something is wrong!");
		}
	});

});

function add_keyword_success(data) {
	alert('Add keyword success!');
	$.mobile.changePage("test.html#keywords", {
		transition : "slideup"
	});
}

// 加载关键字列表
$(document).on("pagebeforeshow", "#keywords", function() {
	//alert("关键字列表即将显示");
	var session_id = localStorage.session_id;
	$.ajax({
		url : 'http://120.27.44.110:5011/mobile/key_word',
		type : 'GET',
		data : {
			session_id : session_id,
		},
		dataType : 'json',
		success : function(data) {
			if (data['ret'] == 0) {
				keyword_success(data);
			} else if (data['ret'] == 1) {
				alert(data['msg']);
			} else {
				alert('Keywords cannot be displayed');
			}
		},
		error : function(e) {
			alert("something is wrong!");
		}
	});
});
function keyword_success(data) {
	var ul = document.getElementById("kwul");
	ul.innerHTML = '';
	data = data['data'];
	for ( var o in data) {
		li = "<li><h2>" + data[o]['kw'] + "</h2></li>";
		ul.innerHTML += li;
	}
	$('#kwul').listview('refresh');
}


//加载标题列表
$(document).on("pagebeforeshow", "#ireads", function() {
	var start_time = getFormatDate();
	//var start_time = "2014-12-29 23:00:00";
	var end_time="2014-12-29 23:00:00";
	var start_num = 1;
	var num = 20;
	var session_id = localStorage.session_id;
	$.ajax({
		url : 'http://120.27.44.110:5011/mobile/content',
		type : 'GET',
		data : {
			session_id : session_id,
			start_time : start_time,
			end_time : end_time,
			start_num : start_num,
			num : num
		},
		dataType : 'json',
		success : function(data) {
			if (data['ret'] == 0) {
				ireads_success(data);
			} else if (data['ret'] == 1) {
				alert(data['msg']);
			} else {
				alert('Keywords cannot be displayed');
			}
		},
		error : function(e) {
			alert("something is wrong!");
		}
	});
});
function ireads_success(data) {
	var ul = document.getElementById("readul");
	ul.innerHTML = '';
	data = data['data'];
	for ( var o in data) {
		li = "<li><a href=\""+ data[o]['url']+"\"><h2>"+data[o]['title']+"</h2><p>"+data[o]['summary']+"</p></a></li>";
		ul.innerHTML += li;
	}
	$('#readul').listview('refresh');
}



function getFormatDate() {
	var day = new Date();
	var Year = 0;
	var Month = 0;
	var Day = 0;
	var Hour = 0;
	var Minute = 0;
	var Second = 0;
	var CurrentDate = "";
	//初始化时间
	Year = day.getFullYear();
	Month = day.getMonth() + 1;
	Day = day.getDate();
	Hour = day.getHours();
	Minute = day.getMinutes();
	Second = day.getSeconds();

	CurrentDate = Year + "-";
	if (Month >= 10) {
		CurrentDate = CurrentDate + Month + "-";
	} else {
		CurrentDate = CurrentDate + "0" + Month + "-";
	}
	if (Day >= 10) {
		CurrentDate = CurrentDate + Day;
	} else {
		CurrentDate = CurrentDate + "0" + Day;
	}

	if (Hour >= 10) {
		CurrentDate = CurrentDate + " " + Hour;
	} else {
		CurrentDate = "0" + Hour;
	}
	if (Minute >= 10) {
		CurrentDate = CurrentDate + ":" + Minute;
	} else {
		CurrentDate = CurrentDate + ":0" + Minute;
	}
	if (Second >= 10) {
		CurrentDate = CurrentDate + ":" + Second;
	} else {
		CurrentDate = CurrentDate + ":0" + Second;
	}
	return CurrentDate;
}

$(document).on("pagebeforeshow", "#me", function() {
	var ul = document.getElementById("meul");
	ul.innerHTML = '';
	li1 = "<li><img src=\"images/star.png\" ><h2>"+localStorage.nickname+"</h2><p>"+localStorage.email+"</p></a></li>";
	li2 = "<li><h2>让我们忠于理想，让我们面对现实！</h2></li>";
	ul.innerHTML += li1;
	ul.innerHTML += li2;
	$('#meul').listview('refresh');
});