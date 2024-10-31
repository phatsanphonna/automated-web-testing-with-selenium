from browser import browser

browser.get('https://ijudge.it.kmitl.ac.th')

assert '<i>Judge' in browser.title

browser.quit()