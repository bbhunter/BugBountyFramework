import reimport subprocessimport configfrom concurrent.futures import ThreadPoolExecutorclass dirb():    def __init__(self):        self.wordlist = config.FILE_LIST	self.threadcount = config.DIRB_THREADS        self.urls = []            def start(self,domain):        output = subprocess.check_output('dirb http://'+domain+' \"'+self.wordlist+'\" -S', shell=True)    	for i in re.findall(r'\+ (.*?) \(C',output):        	self.urls.append(i)                            def run(self,domains):	print '[+]Running dirb with wordlist: '+self.wordlist        tpool = ThreadPoolExecutor(self.threadcount)       	futures = [tpool.submit(self.start,d) for d in domains]	##TODO insert discovered urls into database#	tpool.shutdown(True)	print self.urls	    