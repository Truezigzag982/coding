  //设置标志，用于没有输入时显示0，以及有显示时清空
  var flag = true;

  function calculate(str) {
      var t = document.getElementById("t");
      if (flag) {
          //清除没有输入时的0
          t.value = "";
      }
      //改变状态，不再清空内容
      flag = false;
      //将之前的内容和输入的内容连接起来，重新显示
      t.value = t.value + str; //不是做加法

  }
  //回退一个数，相当于撤销
  function backspace() {
      var t = document.getElementById("t");
      t.value = t.value.substr(0, t.value.length - 1);
  }

  //清空显示内容
  function AC() {
      var t = document.getElementById("t");
      //显示0
      t.value = "0";
      //让下次输入可以清空0
      flag = true;
  }

  //计算结果
  function equals() {
      var t = document.getElementById("t");
      //将字符串转换为逻辑运算
      t.value = eval(t.value);
  }