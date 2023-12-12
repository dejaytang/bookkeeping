import unittest

from analysis.test_analytics import TestAnalysis 
from analysis.test_summary import TestSummaryAnalysis
from analysis.test_budget import TestBudgetAnalysis

from management.test_transaction import TestTransaction
from management.test_book import TestBook

def bookkeeping_suite():
    
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    
    suite.addTest(TestAnalysis('test_loadBookData_expense')) 
    suite.addTest(TestAnalysis('test_loadBookData_income')) 
    suite.addTest(TestAnalysis('test_loadBookData_file_not_found'))
    suite.addTest(TestSummaryAnalysis('test_checkBalance')) 
    suite.addTest(TestBudgetAnalysis('test_setBudget')) 
    suite.addTest(TestBudgetAnalysis('test_overBudgetExpenses'))
    
    suite.addTest(TestTransaction('test_setDate'))
    suite.addTest(TestTransaction('test_setLabel_valid'))
    suite.addTest(TestTransaction('test_setAmount_valid'))
    suite.addTest(TestTransaction('test_toDict'))
    suite.addTest(TestTransaction('test_str'))
    suite.addTest(TestBook('test_addTran_income'))
    suite.addTest(TestBook('test_addTran_expense'))
    suite.addTest(TestBook('test_searchTran_valid'))
    suite.addTest(TestBook('test_searchTran_invalid'))
    suite.addTest(TestBook('test_removeTran_valid'))
    suite.addTest(TestBook('test_clearAll'))
    suite.addTest(TestBook('test_displayBook'))
    
    
    runner = unittest.TextTestRunner() 
    print(runner.run(suite))

bookkeeping_suite()