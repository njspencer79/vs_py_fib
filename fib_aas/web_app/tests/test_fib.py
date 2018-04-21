import unittest
import gmpy
import restcall

hostname = 'http://nginx'

def test_fib_num(n):
    #Tests if number is a Fiboonacci number should be perfect
    #square of (5*n*n + 4) or (5*n*n - 4)

    if gmpy.is_square(5*n*n + 4) or gmpy.is_square(5*n*n - 4):
        return True
    else:
        return False

def test_fib_seq(n):
    str_n = str(n)
    result = restcall.get_url(hostname + '/' + str_n)

    if result == False:
        return False

    for i in result:
        if type(i) != long or test_fib_num(i) == False:

            return False

    #Create a duplicate list to sort to compare sort orders
    sort_result = result
    sort_result.sort()

    if result != sort_result:
        print "Fib numbers not in order."
        return False

    #Check if number of items returns is the same as requested
    if n != 0 and n != len(result):
        print "Number of items don't match."
        return False

    return True


class Test_fibs(unittest.TestCase):

    def test_fib_bad_vals(self):
        #First we throw known garbage values we expect failure each time
        print "\nThis tests each fib number produced. Please wait..."
        print "Testing garbage values - May see HTTP Errors reported\n"
        print "Testing -11"
        self.assertEqual(False, test_fib_seq(-11))
        print "Testing -10000"
        self.assertEqual(False, test_fib_seq(-10000))
        print "Testing #%%"
        self.assertEqual(False, test_fib_seq('#%%'))
        print "Testing 0"
        self.assertEqual(False, test_fib_seq(0))
        print "Testing nate"
        self.assertEqual(False, test_fib_seq('nate'))
        print "Testing 50000"
        self.assertEqual(False, test_fib_seq(50000))
        print "Testing 75000"
        self.assertEqual(False, test_fib_seq(75000))

    def test_fib_good_vals(self):
        print "\n"
        print "Testing valid number of Fib nums to generate\n"

        #We test a small sample against static knownn answers
        print "Testing 8 - Known results"
        tmp_results = [0L, 1L, 1L, 2L, 3L, 5L, 8L, 13L]
        self.assertEqual(tmp_results, restcall.get_url(hostname + '/' + '8'))
        print "Testing 12 - Known results"
        tmp_results = [0L, 1L, 1L, 2L, 3L, 5L, 8L, 13L, 21L, 34L, 55L, 89L]
        self.assertEqual(tmp_results, restcall.get_url(hostname + '/' + '12'))
        print "Testing 15 - Known results"
        tmp_results = [0L, 1L, 1L, 2L, 3L, 5L, 8L, 13L, 21L, 34L, 55L, 89, 144L, 233L, 377L]
        self.assertEqual(tmp_results,  restcall.get_url(hostname + '/' + '15'))

        #we test dynamically.  This will test number of results,
        #each number is a fibonacci, and then the order of the sequence.
        print "\nBeginning Dynamic results testing."
        print "Testing 10"
        self.assertEqual(True, test_fib_seq(10))
        print "Testing 80"
        self.assertEqual(True, test_fib_seq(80))
        print "Testing 200"
        self.assertEqual(True, test_fib_seq(200))
        print "Testing 500"
        self.assertEqual(True, test_fib_seq(500))
        print "Testing 1000"
        self.assertEqual(True, test_fib_seq(1000))
        print "Testing 2500"
        self.assertEqual(True, test_fib_seq(2500))
        print "Testing 5000"
        self.assertEqual(True, test_fib_seq(5000))
        print "Testing 10000"
        self.assertEqual(True, test_fib_seq(10000))
        print "Testing 15000"
        self.assertEqual(True, test_fib_seq(15000))
        print "Testing 20000"
        self.assertEqual(True, test_fib_seq(20000))
        print "Testing 25000"
        self.assertEqual(True, test_fib_seq(25000))
        print "Testing 29000"
        self.assertEqual(True, test_fib_seq(29000))


if __name__ == "__main__":
    unittest.main()
