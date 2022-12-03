//mydate.js
//获取当前日期
function getCurrentDate() {
    var now = new Date();
    var currentDate = "";
    var year = now.getFullYear();
    currentDate += year + "年";
    var month = now.getMonth() + 1;
    currentDate += month + "月";
    var day = now.getDate();
    currentDate += day + "日";
    return currentDate;
}

//获取当前时间, 动态刷新秒数
function getCurrentTime() {
    var now = new Date();
    var hour = now.getHours(); 
    var minu = now.getMinutes(); 
    var sec = now.getSeconds(); 
    if (hour < 10) hour = "0" + hour;
    if (minu < 10) minu = "0" + minu;
    if (sec < 10) sec = "0" + sec;
    var time = hour + ":" + minu + ":" + sec;
    var timeSpan = document.getElementById("curTimeSpan")
    timeSpan.innerHTML = time;
    setTimeout('getCurrentTime()',1000);//每隔1秒加载一次指定函数    
}

//获得星期几相关的下标值
function getWeekdays() {
    this.length = getWeekdays.arguments.length;
    for (var i = 0; i < this.length; i++) {
        this[i] = getWeekdays.arguments[i];
    }
}
