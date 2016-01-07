import sys
import os
import re

'''
Make it so that markdown file of <blg_dir>/_posts/*/_drafts ...
- is moved out of _drafts
- renamed
- replace abspath of image to relative path
'''

input_md_file = os.path.abspath(sys.argv[1])
prj_dir = os.path.dirname(os.path.dirname(input_md_file))
blg_dir = os.path.dirname(os.path.dirname(prj_dir))

newfile = os.path.basename(prj_dir)
newfile = re.sub('_', '-', newfile) + '.md'
newfile = os.path.join(prj_dir, newfile)

with open(newfile, 'w') as out:
    with open(input_md_file) as f:
        content = f.read()
        content = re.sub(blg_dir,
                         '{{ site.baseurl }}',
                         content)
        out.write(content)
