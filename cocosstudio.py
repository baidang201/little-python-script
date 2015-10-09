l = ["Login",
]

l_txt = ["UserName", "Password"]

t_root_layout_head = "Layout* root;"
t_btn_head = "Button*  btn%s;"
t_txt_head = "TextField*  txt%s;"

t_root_layout = r'''root = static_cast<Layout*>(rootNode->getChildByName("root"));'''
t = '''
	btn%s = static_cast<Button*> (Helper::seekWidgetByName(root, "btn%s"));
	btn%s->setTouchEnabled(true);
	btn%s->addTouchEventListener(CC_CALLBACK_2(HelloWorld::%sEvent, this));
	'''
t_txt = '''
	txt%s = static_cast<TextField*> (Helper::seekWidgetByName(root, "txt%s"));
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
print t_root_layout_head
for item in l:
    print t_btn_head %(item)

for item in l_txt:
    print t_txt_head %(item)
    
###############################    
print t_root_layout
for item in l:
    print t %(item, item, item, item, item)

for item in l_txt:
    print t_txt %(item, item)
###################################
for item in l:
    print t2 %(item)
######################################
for item in l:
    print t3 %(item)
############################
