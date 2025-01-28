import 'package:flame/game.dart';
import 'package:flame/components.dart';
import 'package:flame/input.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(GameWidget(game: The4DirectionsGame()));
}  

class The4DirectionsGame extends FlameGame with HasCollisionDetection {
  late SpriteComponent bunny;
  late JoystickComponent joystick;

  @override
  Future<void> onLoad() async {
    final background = SpriteComponent(
      sprite: await Sprite.load('background.png'),
      size: canvasSize,
    );
    add(background);

    // Load the bunny sprite
    bunny = SpriteComponent(
      sprite: await Sprite.load('bunny.png'),
      position: Vector2(200, 200),
      size: Vector2(100, 100),
    );
    add(bunny);

  
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

  @override
  void update(double dt) {
    super.update(dt);

    if (joystick.direction != JoystickDirection.idle) {
      bunny.position.add(joystick.relativeDelta * 100 * dt);
    }
  }
}
