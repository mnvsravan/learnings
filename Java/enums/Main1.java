// ============================================================
//       ENUM WITH ABSTRACT METHOD + OVERRIDING
// ============================================================
//
// Each enum constant can have its OWN implementation of a
// method.
//
// Here:
//
//     NORTH → move() → "Moving Up"
//     SOUTH → move() → "Moving Down"
//     EAST  → move() → "Moving Right"
//     WEST  → move() → "Moving Left"
//
// ============================================================

public class Main1 {

    enum Direction {

        // ----------------------------------------------------
        // NORTH
        // ----------------------------------------------------
        //
        // NORTH is an enum object.
        //
        // It provides its own implementation of move().
        //

        NORTH {

            @Override
            public void move() {
                System.out.println("Moving Up");
            }
        },


        // ----------------------------------------------------
        // SOUTH
        // ----------------------------------------------------

        SOUTH {

            @Override
            public void move() {
                System.out.println("Moving Down");
            }
        },


        // ----------------------------------------------------
        // EAST
        // ----------------------------------------------------

        EAST {

            @Override
            public void move() {
                System.out.println("Moving Right");
            }
        },


        // ----------------------------------------------------
        // WEST
        // ----------------------------------------------------

        WEST {

            @Override
            public void move() {
                System.out.println("Moving Left");
            }
        };


        // ----------------------------------------------------
        // ABSTRACT METHOD
        // ----------------------------------------------------
        //
        // Every enum constant MUST provide its own
        // implementation of this method.
        //
        // Why?
        //
        // Because NORTH, SOUTH, EAST and WEST all behave
        // differently when move() is called.
        //
        // ----------------------------------------------------

        public abstract void move();
    }


    public static void main(String[] args) {

        // d refers to the NORTH enum object.

        Direction d = Direction.NORTH;

        d.move();

        // Output:
        // Moving Up


        // Change d to SOUTH.

        d = Direction.SOUTH;

        d.move();

        // Output:
        // Moving Down


        // Change d to EAST.

        d = Direction.EAST;

        d.move();

        // Output:
        // Moving Right


        // Change d to WEST.

        d = Direction.WEST;

        d.move();

        // Output:
        // Moving Left
    }
}
