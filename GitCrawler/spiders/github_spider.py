import scrapy
import json
from datetime import datetime


class GithubSpider(scrapy.Spider):
    name = "git"   # give the spider name
    allowed_domains = ["github.com"]
    pagecount = 1   # initially start crawling from page 1
    current_date = datetime.now()
    result = {'totalIssue' : 0,'In24Hours' : 0,'Between7To1' : 0,'Before7' : 0}   #  dictionary to store the data
    # print "current date1 is %s" % current_date

    #take the sent url  [like  = https://github.com/Shippable/support]
    def __init__(self,domain=''):        
        self.url = domain + "/issues"    

    #function for starting crawling for first page 
    def start_requests(self):
        yield scrapy.Request(self.url, self.parse)   

    #Function to parse the page and extract the usefull information
    def parse(self, response):        
        OneTo7Days = 0
        LessThan1Days = 0 
        Prev_After7Days = 0

        for sel in response.xpath('//div/span'):
        	#Extract  Date and time from page
            DateFrompage = sel.xpath('time/text()').extract()
            TimeFormPage = sel.xpath('time/@datetime').extract()
            if (DateFrompage):              
                dateString = TimeFormPage[0].split('T')
                timeString = dateString[1].split('Z')
                CombineDate = dateString[0] + " " + timeString[0]               
                #Final formatted date form page
                Git_date = datetime.strptime(CombineDate,'%Y-%m-%d %H:%M:%S')
                diff = self.current_date - Git_date
                #when Issue was created in preve 24 hours     
                if (diff.days <= 1):
                    LessThan1Days = LessThan1Days + 1
                #when Issue was created before 24 hours and after 7 days     
                elif(diff.days >= 1 and diff.days <= 7): 
                    OneTo7Days  = OneTo7Days + 1
                #when Issue was created before 7 days
                else: 
                    Prev_After7Days  = Prev_After7Days + 1
                
        #store the information in result from each page             
        self.result['In24Hours'] = self.result['In24Hours'] + LessThan1Days
        self.result['Between7To1'] = self.result['Between7To1'] + OneTo7Days
        self.result['Before7'] = self.result['Before7'] + Prev_After7Days

        total = LessThan1Days + OneTo7Days + Prev_After7Days
        self.result['totalIssue'] = self.result['totalIssue'] + total
        
        #IF next page contains issues then extract info else stop
        if total > 0 :            
            self.pagecount = self.pagecount + 1
            self.next_url = self.url + "?page="+ (self.pagecount).__str__()
            #request sent for next page            
            yield scrapy.Request(self.next_url, self.parse)
        else:
            self.display()

  
    
    def display(self):
        print "\nTotal Open Issues : ", self.result['totalIssue']
        print "\nIssues opened in prev 24 Hours : ", self.result['In24Hours']
        print "\nIssues opened Before 24 hours and after 7 days : ",self.result['Between7To1']
        print "\nIssues opened prev before 7 days : ",self.result['Before7']
        print "\n"
