I have started this task by adding background
```dart
 Future<void> onLoad() async {
    final background = SpriteComponent(
      sprite: await Sprite.load('background.png'),
      size: canvasSize,
    );
    add(background);
    ```


Then i have added bunny which is declared earlier as late SpriteComponent bunny which declares that it is a movable componenent
```dart
    bunny = SpriteComponent(
      sprite: await Sprite.load('bunny.png'),
      position: Vector2(200, 200),
      size: Vector2(100, 100),
    );
    add(bunny);
```


Then i have added joystick at the center of screen
```dart
   joystick = JoystickComponent(
      knob: CircleComponent(
        radius: 15,
        paint: Paint()..color = Colors.blue,
      ),
      background: CircleComponent(
        radius: 40,
        paint: Paint()..color = Colors.grey,
      ),
    )
      ..position = size/2;
    add(joystick);
  }
  ```


with this part, position of spirit is changed upon interacting with joystick
```dart
  @override
  void update(double dt) {
    super.update(dt);

    if (joystick.direction != JoystickDirection.idle) {
      bunny.position.add(joystick.relativeDelta * 100 * dt);
    }
  }
```


here is a video of [mini game](video.mp4) (I could not record on my laptop due to storage issues so i have to record in phone)
