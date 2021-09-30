from flask import Flask, jsonify, request
import subprocess
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_tasks():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        # return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
        # return request.environ['REMOTE_ADDR'] + '\n', 200
        myip = request.environ['REMOTE_ADDR']
    else:
        # return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200
        # return request.environ['HTTP_X_FORWARDED_FOR'] + '\n', 200
        myip = request.environ['HTTP_X_FORWARDED_FOR']
    tccli_command = subprocess.Popen('tccli lighthouse CreateFirewallRules --cli-unfold-argument --region ap-hongkong --InstanceId lhins-jjbknicj --FirewallRules.0.Protocol TCP --FirewallRules.0.Port 1080 --FirewallRules.0.CidrBlock {}/32 --FirewallRules.0.Action ACCEPT 2>&1'.format(myip), stdout=subprocess.PIPE, shell=True)
    return tccli_command.stdout.read()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=7070)
