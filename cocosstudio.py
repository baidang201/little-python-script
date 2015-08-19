l = ["Play",
"Pause",
"Resume",
"Stop",
"Effect",]


t = '''
	btn%s = static_cast<Button*> (Helper::seekWidgetByName(root, "btn%s"));
	btn%s->setTouchEnabled(true);
	btn%s->addTouchEventListener(CC_CALLBACK_2(HelloWorld::%sEvent, this));
	'''


t2 = '''
void HelloWorld::%sEvent(Ref* pSender, Widget::TouchEventType type)
{
	if(type == Widget::TouchEventType::ENDED)
	{
		 
	}
}
'''

t3 = '''
void %sEvent(Ref* pSender, Widget::TouchEventType type);
'''
for item in l:
    print t %(item, item, item, item, item)

for item in l:
    print t2 %(item)

for item in l:
    print t3 %(item)
