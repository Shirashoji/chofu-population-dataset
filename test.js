var str = "100+";
// var str = "10-20";
var result = str
  .replace(/(\d*)-(\d*)/g, "$1~$2歳")
  .replace(/(\d*)\+/g, "$1歳以上");
console.log(result); // 結果: 10~20歳
