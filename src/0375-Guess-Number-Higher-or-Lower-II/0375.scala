object Solution{
  def getMontyAmount(n:Int):Int = {
    val dp = Array.ofDim[Int](n+1,n+1)
    for(l <- (n-1).to(1).by(-1)){
      for(r <- (l+1).to(n).by(1)){
        var tmp = List[Int]()
        for(i <- l.to(r-1).by(1)) {
          tmp ::= (i + (dp(l)(i-1)).max(dp(i+1)(r)))
        }
        dp(l)(r) = tmp.min
      }
    }
    dp(1)(n)
  }

  def main(args:Array[String]): Unit ={
    val n = 10
    println(getMontyAmount(n))
  }
}