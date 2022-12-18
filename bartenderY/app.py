from flask import Flask, request
from flask_cors import CORS
import model

app = Flask(__name__)
CORS(app)

def model_predit(user_keyword):

    # don't know what is the output of model yet
    keyword_cocktail = [
        {
            "name":"57 Chevy",
            "image":"https://cocktail-conference-bucket.s3.ap-northeast-2.amazonaws.com/3%EB%8C%804.jpg"
        },
        {
            "name":"Caipirinha",
            "image":"https://cocktail-conference-bucket.s3.ap-northeast-2.amazonaws.com/3%EB%8C%804.jpg"
        },
        {
            "name":"Long Island Icetea",
            "image":"https://cocktail-conference-bucket.s3.ap-northeast-2.amazonaws.com/3%EB%8C%804.jpg"
        },
        {
            "name":"Piña Colada",
            "image":"https://cocktail-conference-bucket.s3.ap-northeast-2.amazonaws.com/3%EB%8C%804.jpg"
        },
        {
            "name":"Tall Blonde",
            "image":"https://cocktail-conference-bucket.s3.ap-northeast-2.amazonaws.com/3%EB%8C%804.jpg"
       }
    ]

    return keyword_cocktail


@app.route('/search', methods= ['GET'])
def model_result():
    if request.method == 'GET' :
        keyword = request.args.get('keyword')
        
        recommend_list = model.model_call(keyword)

        result = list()

        for i in range(5) :
            this_name = recommend_list[i]["이름 (영어)"]
            # print(recommend_list[i]["이름 (영어)"])
            this_image = recommend_list[i]["사진링크"]
            
            this_dict = dict()
            this_dict['name'] = this_name
            this_dict['image'] = this_image

            result.append(this_dict)

        return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = False)
