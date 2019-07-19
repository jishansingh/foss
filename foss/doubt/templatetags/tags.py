from django import template
import re
register=template.Library()
@register.filter(name='split_tags')
def split_tags(value):
        value=value.replace('\n','')
        value=value.replace('\r','')
        print(value)
        ans=value.split('*')
        some=re.compile('\*(<.{1,4}?>)\*')
        some=some.findall(value)
        total=[]
        print(some)
        for one in ans:
                er=False
                if one in some and 'script' not in one:
                        er=True
                pink={one:er}
                total.append(pink)
        print(total)

        return total
