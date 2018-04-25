from PIL import Image, ImageDraw
import sys
import json
import boto3

im = Image.open("faces.jpg")

jsonData = '''{
    "FaceDetails": [
        {
            "BoundingBox": {
                "Width": 0.2527777850627899,
                "Height": 0.3791666626930237,
                "Left": 0.0694444477558136,
                "Top": 0.27222222089767456
            },
            "AgeRange": {
                "Low": 45,
                "High": 63
            },
            "Smile": {
                "Value": true,
                "Confidence": 99.92107391357422
            },
            "Eyeglasses": {
                "Value": false,
                "Confidence": 99.98888397216797
            },
            "Sunglasses": {
                "Value": false,
                "Confidence": 98.81751251220703
            },
            "Gender": {
                "Value": "Male",
                "Confidence": 99.9273681640625
            },
            "Beard": {
                "Value": true,
                "Confidence": 99.89876556396484
            },
            "Mustache": {
                "Value": true,
                "Confidence": 74.63887023925781
            },
            "EyesOpen": {
                "Value": false,
                "Confidence": 98.88184356689453
            },
            "MouthOpen": {
                "Value": false,
                "Confidence": 92.01380920410156
            },
            "Emotions": [
                {
                    "Type": "HAPPY",
                    "Confidence": 99.41680145263672
                },
                {
                    "Type": "DISGUSTED",
                    "Confidence": 3.642451763153076
                },
                {
                    "Type": "CONFUSED",
                    "Confidence": 0.39097070693969727
                }
            ],
            "Landmarks": [
                {
                    "Type": "eyeLeft",
                    "X": 0.17077851295471191,
                    "Y": 0.3949631154537201
                },
                {
                    "Type": "eyeRight",
                    "X": 0.24877072870731354,
                    "Y": 0.42977315187454224
                },
                {
                    "Type": "nose",
                    "X": 0.2204890251159668,
                    "Y": 0.4564211666584015
                },
                {
                    "Type": "mouthLeft",
                    "X": 0.1433829516172409,
                    "Y": 0.5137478113174438
                },
                {
                    "Type": "mouthRight",
                    "X": 0.23381458222866058,
                    "Y": 0.5534982681274414
                },
                {
                    "Type": "leftPupil",
                    "X": 0.17245598137378693,
                    "Y": 0.39451056718826294
                },
                {
                    "Type": "rightPupil",
                    "X": 0.24685823917388916,
                    "Y": 0.42825427651405334
                },
                {
                    "Type": "leftEyeBrowLeft",
                    "X": 0.14452949166297913,
                    "Y": 0.3546369671821594
                },
                {
                    "Type": "leftEyeBrowUp",
                    "X": 0.17308127880096436,
                    "Y": 0.33538997173309326
                },
                {
                    "Type": "leftEyeBrowRight",
                    "X": 0.20340277254581451,
                    "Y": 0.3483930826187134
                },
                {
                    "Type": "rightEyeBrowLeft",
                    "X": 0.24135860800743103,
                    "Y": 0.36609676480293274
                },
                {
                    "Type": "rightEyeBrowUp",
                    "X": 0.26588955521583557,
                    "Y": 0.3781099021434784
                },
                {
                    "Type": "rightEyeBrowRight",
                    "X": 0.28051915764808655,
                    "Y": 0.41244739294052124
                },
                {
                    "Type": "leftEyeLeft",
                    "X": 0.1539274901151657,
                    "Y": 0.39252081513404846
                },
                {
                    "Type": "leftEyeRight",
                    "X": 0.18769589066505432,
                    "Y": 0.40090763568878174
                },
                {
                    "Type": "leftEyeUp",
                    "X": 0.17099739611148834,
                    "Y": 0.38976889848709106
                },
                {
                    "Type": "leftEyeDown",
                    "X": 0.1705264449119568,
                    "Y": 0.3984062075614929
                },
                {
                    "Type": "rightEyeLeft",
                    "X": 0.23332875967025757,
                    "Y": 0.4223070740699768
                },
                {
                    "Type": "rightEyeRight",
                    "X": 0.26322248578071594,
                    "Y": 0.4420147240161896
                },
                {
                    "Type": "rightEyeUp",
                    "X": 0.2496660053730011,
                    "Y": 0.4247362017631531
                },
                {
                    "Type": "rightEyeDown",
                    "X": 0.24837064743041992,
                    "Y": 0.4324222505092621
                },
                {
                    "Type": "noseLeft",
                    "X": 0.186639666557312,
                    "Y": 0.4738188087940216
                },
                {
                    "Type": "noseRight",
                    "X": 0.22678376734256744,
                    "Y": 0.48992887139320374
                },
                {
                    "Type": "mouthUp",
                    "X": 0.19846610724925995,
                    "Y": 0.5114622116088867
                },
                {
                    "Type": "mouthDown",
                    "X": 0.1840672641992569,
                    "Y": 0.5700075030326843
                }
            ],
            "Pose": {
                "Roll": 14.86003589630127,
                "Yaw": 21.071380615234375,
                "Pitch": 24.002830505371094
            },
            "Quality": {
                "Brightness": 45.9872932434082,
                "Sharpness": 99.80813598632812
            },
            "Confidence": 99.9966049194336
        },
        {
            "BoundingBox": {
                "Width": 0.192592591047287,
                "Height": 0.2888889014720917,
                "Left": 0.7435185313224792,
                "Top": 0.4749999940395355
            },
            "AgeRange": {
                "Low": 26,
                "High": 43
            },
            "Smile": {
                "Value": true,
                "Confidence": 99.69186401367188
            },
            "Eyeglasses": {
                "Value": false,
                "Confidence": 99.99881744384766
            },
            "Sunglasses": {
                "Value": false,
                "Confidence": 99.9429931640625
            },
            "Gender": {
                "Value": "Female",
                "Confidence": 100
            },
            "Beard": {
                "Value": false,
                "Confidence": 99.25056457519531
            },
            "Mustache": {
                "Value": false,
                "Confidence": 99.96064758300781
            },
            "EyesOpen": {
                "Value": false,
                "Confidence": 97.60916900634766
            },
            "MouthOpen": {
                "Value": false,
                "Confidence": 99.57764434814453
            },
            "Emotions": [
                {
                    "Type": "HAPPY",
                    "Confidence": 99.90779113769531
                },
                {
                    "Type": "SAD",
                    "Confidence": 1.9382596015930176
                },
                {
                    "Type": "CALM",
                    "Confidence": 0.36217570304870605
                }
            ],
            "Landmarks": [
                {
                    "Type": "eyeLeft",
                    "X": 0.7982872128486633,
                    "Y": 0.5955836176872253
                },
                {
                    "Type": "eyeRight",
                    "X": 0.866336464881897,
                    "Y": 0.5779889225959778
                },
                {
                    "Type": "nose",
                    "X": 0.8308957815170288,
                    "Y": 0.634591817855835
                },
                {
                    "Type": "mouthLeft",
                    "X": 0.8094145655632019,
                    "Y": 0.6926126480102539
                },
                {
                    "Type": "mouthRight",
                    "X": 0.879722535610199,
                    "Y": 0.6788098812103271
                },
                {
                    "Type": "leftPupil",
                    "X": 0.8032697439193726,
                    "Y": 0.5952105522155762
                },
                {
                    "Type": "rightPupil",
                    "X": 0.8696646690368652,
                    "Y": 0.5805066823959351
                },
                {
                    "Type": "leftEyeBrowLeft",
                    "X": 0.7691576480865479,
                    "Y": 0.5762478113174438
                },
                {
                    "Type": "leftEyeBrowUp",
                    "X": 0.7863252758979797,
                    "Y": 0.5552977919578552
                },
                {
                    "Type": "leftEyeBrowRight",
                    "X": 0.8092250823974609,
                    "Y": 0.5560559034347534
                },
                {
                    "Type": "rightEyeBrowLeft",
                    "X": 0.8466066718101501,
                    "Y": 0.5451985001564026
                },
                {
                    "Type": "rightEyeBrowUp",
                    "X": 0.8700916171073914,
                    "Y": 0.5347290635108948
                },
                {
                    "Type": "rightEyeBrowRight",
                    "X": 0.8912621736526489,
                    "Y": 0.5499251484870911
                },
                {
                    "Type": "leftEyeLeft",
                    "X": 0.7860785126686096,
                    "Y": 0.6009538173675537
                },
                {
                    "Type": "leftEyeRight",
                    "X": 0.8111250400543213,
                    "Y": 0.5929529666900635
                },
                {
                    "Type": "leftEyeUp",
                    "X": 0.7975198030471802,
                    "Y": 0.5903558731079102
                },
                {
                    "Type": "leftEyeDown",
                    "X": 0.7987400889396667,
                    "Y": 0.5994415879249573
                },
                {
                    "Type": "rightEyeLeft",
                    "X": 0.8537998199462891,
                    "Y": 0.5822697877883911
                },
                {
                    "Type": "rightEyeRight",
                    "X": 0.8797850012779236,
                    "Y": 0.5765429735183716
                },
                {
                    "Type": "rightEyeUp",
                    "X": 0.8654080033302307,
                    "Y": 0.5723800659179688
                },
                {
                    "Type": "rightEyeDown",
                    "X": 0.8668090105056763,
                    "Y": 0.5821802616119385
                },
                {
                    "Type": "noseLeft",
                    "X": 0.8233538866043091,
                    "Y": 0.6573517918586731
                },
                {
                    "Type": "noseRight",
                    "X": 0.8537777066230774,
                    "Y": 0.6485087275505066
                },
                {
                    "Type": "mouthUp",
                    "X": 0.8413063287734985,
                    "Y": 0.679395318031311
                },
                {
                    "Type": "mouthDown",
                    "X": 0.8464540243148804,
                    "Y": 0.7106876969337463
                }
            ],
            "Pose": {
                "Roll": -9.95767593383789,
                "Yaw": -6.593029499053955,
                "Pitch": 3.8418571949005127
            },
            "Quality": {
                "Brightness": 50.12673568725586,
                "Sharpness": 99.884521484375
            },
            "Confidence": 99.99989318847656
        },
        {
            "BoundingBox": {
                "Width": 0.16203702986240387,
                "Height": 0.24444444477558136,
                "Left": 0.38148146867752075,
                "Top": 0.49166667461395264
            },
            "AgeRange": {
                "Low": 2,
                "High": 5
            },
            "Smile": {
                "Value": true,
                "Confidence": 98.89238739013672
            },
            "Eyeglasses": {
                "Value": false,
                "Confidence": 99.12181854248047
            },
            "Sunglasses": {
                "Value": false,
                "Confidence": 99.5721435546875
            },
            "Gender": {
                "Value": "Female",
                "Confidence": 100
            },
            "Beard": {
                "Value": false,
                "Confidence": 99.2862548828125
            },
            "Mustache": {
                "Value": false,
                "Confidence": 99.99153137207031
            },
            "EyesOpen": {
                "Value": true,
                "Confidence": 87.98113250732422
            },
            "MouthOpen": {
                "Value": false,
                "Confidence": 58.798152923583984
            },
            "Emotions": [
                {
                    "Type": "HAPPY",
                    "Confidence": 25.60356903076172
                },
                {
                    "Type": "SAD",
                    "Confidence": 2.915292978286743
                },
                {
                    "Type": "CONFUSED",
                    "Confidence": 2.347332239151001
                }
            ],
            "Landmarks": [
                {
                    "Type": "eyeLeft",
                    "X": 0.4384130537509918,
                    "Y": 0.585084855556488
                },
                {
                    "Type": "eyeRight",
                    "X": 0.49115172028541565,
                    "Y": 0.5859259963035583
                },
                {
                    "Type": "nose",
                    "X": 0.46652254462242126,
                    "Y": 0.605634331703186
                },
                {
                    "Type": "mouthLeft",
                    "X": 0.4558124244213104,
                    "Y": 0.6833081841468811
                },
                {
                    "Type": "mouthRight",
                    "X": 0.48030948638916016,
                    "Y": 0.6794667840003967
                },
                {
                    "Type": "leftPupil",
                    "X": 0.435606986284256,
                    "Y": 0.5839483737945557
                },
                {
                    "Type": "rightPupil",
                    "X": 0.4958358705043793,
                    "Y": 0.5847238302230835
                },
                {
                    "Type": "leftEyeBrowLeft",
                    "X": 0.4161299169063568,
                    "Y": 0.5649797916412354
                },
                {
                    "Type": "leftEyeBrowUp",
                    "X": 0.4303557872772217,
                    "Y": 0.5494264960289001
                },
                {
                    "Type": "leftEyeBrowRight",
                    "X": 0.44805461168289185,
                    "Y": 0.5456513166427612
                },
                {
                    "Type": "rightEyeBrowLeft",
                    "X": 0.4791647493839264,
                    "Y": 0.5472806096076965
                },
                {
                    "Type": "rightEyeBrowUp",
                    "X": 0.49530792236328125,
                    "Y": 0.5463719964027405
                },
                {
                    "Type": "rightEyeBrowRight",
                    "X": 0.5086570978164673,
                    "Y": 0.5589195489883423
                },
                {
                    "Type": "leftEyeLeft",
                    "X": 0.42798978090286255,
                    "Y": 0.5874162316322327
                },
                {
                    "Type": "leftEyeRight",
                    "X": 0.44842100143432617,
                    "Y": 0.584660530090332
                },
                {
                    "Type": "leftEyeUp",
                    "X": 0.43816590309143066,
                    "Y": 0.5792652368545532
                },
                {
                    "Type": "leftEyeDown",
                    "X": 0.43886786699295044,
                    "Y": 0.5899507999420166
                },
                {
                    "Type": "rightEyeLeft",
                    "X": 0.4807860255241394,
                    "Y": 0.5857197642326355
                },
                {
                    "Type": "rightEyeRight",
                    "X": 0.501345157623291,
                    "Y": 0.5871026515960693
                },
                {
                    "Type": "rightEyeUp",
                    "X": 0.491178035736084,
                    "Y": 0.5809101462364197
                },
                {
                    "Type": "rightEyeDown",
                    "X": 0.49121150374412537,
                    "Y": 0.590456485748291
                },
                {
                    "Type": "noseLeft",
                    "X": 0.4581461548805237,
                    "Y": 0.6345648169517517
                },
                {
                    "Type": "noseRight",
                    "X": 0.475790411233902,
                    "Y": 0.63379967212677
                },
                {
                    "Type": "mouthUp",
                    "X": 0.4670886695384979,
                    "Y": 0.651400089263916
                },
                {
                    "Type": "mouthDown",
                    "X": 0.4693535566329956,
                    "Y": 0.6827617883682251
                }
            ],
            "Pose": {
                "Roll": 0.012837439775466919,
                "Yaw": 2.404158115386963,
                "Pitch": 22.07772445678711
            },
            "Quality": {
                "Brightness": 53.478179931640625,
                "Sharpness": 99.884521484375
            },
            "Confidence": 99.96392822265625
        }
    ],
    "OrientationCorrection": "ROTATE_0"
}'''
faceObj = json.loads(jsonData)

draw = ImageDraw.Draw(im)

# Convert fractional bounding box coordinates from recognition and convert to absolute pixals
def computeRectangleCoordinates(image, face):
    # Extract fractional values
    left   = face['BoundingBox']['Left']
    top    = face['BoundingBox']['Top']
    width  = face['BoundingBox']['Width']
    height = face['BoundingBox']['Height']
    # Convert fractional values to pixel values
    x0 = (int)(image.width*left)
    y0 = (int)(image.height*top)
    x1 = (int)(x0 + image.width*width)
    y1 = (int)(y0 + image.height*height)
    return [x0, y0, x1, y1]


# Get face bounding box cordinates from rek reponse and iterate over them to draw boxes on image
for faceCords in faceObj['FaceDetails']:
    coOrds = computeRectangleCoordinates(im, faceCords)
    coOrds1 = [x+1 for x in coOrds]
    coOrds2 = [x+2 for x in coOrds]
    coOrds3 = [x+3 for x in coOrds]
    draw.rectangle(coOrds, outline="yellow")
    draw.rectangle(coOrds1, outline="yellow")
    draw.rectangle(coOrds2, outline="yellow")
    draw.rectangle(coOrds3, outline="yellow")

del draw

# write to stdout
im.save('faces.png', "PNG")
