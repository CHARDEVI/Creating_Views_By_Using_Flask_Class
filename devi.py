from flask import Flask

FAI=Flask(__name__)

@FAI.route('/wish')
def wish():
    return 'This is Our First Flask Class'


@FAI.route('/wish2')
def wish2():
    return 'This is Our Last Django Class'

if __name__=='__main__':
    FAI.run(debug=True)






    



