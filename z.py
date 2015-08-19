'''
for i in range(0, 10):
    print "%d>= listSum.Count()? \"0\": listSum[%d].ToString()," %(i, i),
    '''

l = ["One", "Two", "Three", "Four", "Five"]
tep = '''
  protected string m_%s = "";
        public string %s
        {
            get { return this.m_%s; }
            set
            {
                this.m_%s = value;
                NotifyPropertyChanged("%s");
            }
        }
        '''

for item in l:
    print tep %(item, item, item, item, item)
