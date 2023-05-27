import re

txt = input()
l = 'abcdefghijklmnopqrstuvwxyz'

result = re.match('^a* *b* *c* *d* *e* *f* *g* *h* *i* *j* *k* *l* *m* *n* *o* *p* *q* *r* *s* *t* *u* *v* *w* *x* *y* *z* *$', txt)

print(bool(result))