object Solution{
  def wiggleMaxLength(nums:Array[Int]): Int ={
    var _pos, _neg = 1
    for(i <- 1 until nums.length){
      if(nums(i-1) < nums(i)){
        _neg = _pos + 1
      }else if(nums(i-1) < nums(i)) {
        _pos = _neg + 1
      }
    }
    return if (_neg > _pos) _neg else _pos
  }

  def main(args:Array[String]): Unit ={
    val nums = Array(1,17,5,10,13,15,10,5,16,8)
    println(wiggleMaxLength(nums))
  }
}