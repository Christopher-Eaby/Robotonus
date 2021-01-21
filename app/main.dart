import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';
import 'dart:async';

void main() {
  runApp(MaterialApp(
    initialRoute: '/',
    routes: {
      '/': (context) => HomeRoute(),
      '/second': (context) => SecondRoute(),
      '/third': (context) => ThirdRoute(),
    },
  ));
}

class HomeRoute extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Robotonus'),
        backgroundColor: Colors.blue,
      ),
      body: Center(
          child: Column(
            children: <Widget>[
              RaisedButton(
                child: Text('Mines Database Map'),
                onPressed: () {
                  Navigator.pushNamed(context, '/second');
                },
              ),
              RaisedButton(
                child: Text('Controls'),
                onPressed: () {
                  Navigator.pushNamed(context, '/third');
                },
              ),
            ],
          )),
    );
  }
}

class SecondRoute extends StatelessWidget {
  final Completer<WebViewController> _controller =
  Completer<WebViewController>();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Mines Database Map"),
          backgroundColor: Colors.blue,
        ),
        body: WebView(
          initialUrl: "https://robotonus.tiiny.site/",
          javascriptMode: JavascriptMode.unrestricted,
          onWebViewCreated: (WebViewController webViewController) {
            _controller.complete(webViewController);
          },
        ));
  }
}

class ThirdRoute extends StatelessWidget {
  final Completer<WebViewController> _controller =
  Completer<WebViewController>();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Controls"),
        backgroundColor: Colors.blue,
      ),
      body: Column(children: <Widget>[
        Container(
          height: 250,
          child: WebView(
            initialUrl: "https://www.youtube.com/watch?v=D4wF0snbC00&ab_channel=PBSNewsHour",
            javascriptMode: JavascriptMode.unrestricted,
            onWebViewCreated: (WebViewController webViewController) {
              _controller.complete(webViewController);
            },
          ),
        ),
        IconButton(
          onPressed: () {
            print('forward');
          },
          icon: Icon(Icons.arrow_circle_up),
          iconSize: 100,
        ),
        Row(children: <Widget>[
          IconButton(
            onPressed: () {
              print('left');
            },
            icon: Icon(Icons.arrow_back),
            iconSize: 100,
          ),
          IconButton(
            onPressed: () {
              print('right');
            },
            icon: Icon(Icons.arrow_forward),
            iconSize: 100,
          ),
        ]),
        IconButton(
          onPressed: () {
            print('backwards');
          },
          icon: Icon(Icons.arrow_circle_down),
          iconSize: 100,
        ),
        FlatButton(
          child: new Text('Test For Mine Detection'),
          onPressed: () {
            showDialog(
                context: context,
                builder: (BuildContext context) {
                  return AlertDialog(
                    title: Text('Mine Detected!'),
                    content: Text(
                        'Either accept or log a new mine in the database. NB: DB functionality not yet active'),
                    actions: [
                      FlatButton(
                        child: Text('Accept'),
                        onPressed: () => Navigator.pop(context),
                      ),
                      FlatButton(
                        child: Text('Log new Mine'),
                        onPressed: () => Navigator.pop(context),
                        //Ask Boiseman how to print/insert record into db
                      ),
                    ],
                  );
                });
          },
        ),
      ]),
    );
  }
}

// AlertDialog test = AlertDialog(
// title: Text('Mine Detected!'),
// content: Text(
// 'Either accept or log a new mine in the database. NB: DB functionality not yet active'),
// actions: [
//   FlatButton(
//     child: Text('Accept'),
//   ),
//   FlatButton(
//     child: Text('Log new Mine'),
//   ),
// ],
// );
//
// showDialog(
// context: context,
// builder: (BuildContext context) {
// return test;
// },
// );
// }
// AlertDialog test = AlertDialog(
// title: Text('Mine Detected!'),
// content: Text(
// 'Either accept or log a new mine in the database. NB: DB functionality not yet active'),
// actions: [
//   FlatButton(
//     child: Text('Accept'),
//   ),
//   FlatButton(
//     child: Text('Log new Mine'),
//   ),
// ],
// );
//
// showDialog(
// context: context,
// builder: (BuildContext context) {
// return test;
// },
// );
// }// import 'package:flutter/material.dart';
//
// void main() => runApp(new MyApp());
//
// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return new MaterialApp(
//       home: Scaffold(
//         appBar: AppBar(
//           title: Text('Robotonus Controller'),
//         ),
//         body: Column(children: <Widget>[
//           IconButton(
//             onPressed: () {
//               print('forward');
//             },
//             icon: Icon(Icons.arrow_circle_up),
//             iconSize: 150,
//           ),
//           Row(children: <Widget>[
//             IconButton(
//               onPressed: () {
//                 print('left');
//               },
//               icon: Icon(Icons.arrow_back),
//               iconSize: 150,
//             ),
//             IconButton(
//               onPressed: () {
//                 print('right');
//               },
//               icon: Icon(Icons.arrow_forward),
//               iconSize: 150,
//             ),
//           ]),
//           IconButton(
//             onPressed: () {
//               print('backwards');
//             },
//             icon: Icon(Icons.arrow_circle_down),
//             iconSize: 150,
//           ),
//         ]),
//       ),
//     );
//   }
// }
