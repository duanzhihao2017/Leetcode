object Solution{
  def combinationSum4(nums:Array[Int], target:Int): Int ={
    val dp:Array[Int] = Array.fill[Int](target+1)(0)
    dp(0) = 1
    for(i <- 1 until target+1){
      for(num <- nums){
        if(i - num >= 0){
          dp(i) += dp(i-num)
        }
      }
    }
    dp(target)
  }

  def main(args:Array[String]): Unit ={
    val nums = Array(1,2,3)
    val target = 4
    println(combinationSum4(nums, target))
  }
}