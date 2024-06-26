object  exampleFunction:
    def main(args: Array[String]) ={
        printPrimeNums(primeNums)
        println("Hello World")
        println(add(1,2))
        println("Closure:\t" + multiplier(3))
        println(m)
        println("Double or Nothing:\t" + doubleOrNothing)
    }


    //Functions
    def add(a:Int, b:Int): Int = {
        return a + b
    }

    // Closure
    var factor = 3
    val multiplier = (number:Int) => number * factor;

    //Anoymous Function or Lambdas
    val anonList = List(1,2,3,4,5)
    val doubleOrNothing = anonList.map(_ * 2)


    //For Loop 
    val primeNums = Seq(2,3,5,7,11)
    def printPrimeNums(nums:Seq[Int]):Unit = {
        for i <- nums do println(i)
    }

    // For each expression with yield keyword
    val m:IndexedSeq[Int] = for (i <- 0 to 5) yield i * 2

end exampleFunction






