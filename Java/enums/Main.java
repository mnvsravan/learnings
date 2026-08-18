// ============================================================
//                 ENUM WITH FIELDS + CONSTRUCTOR
// ============================================================
//
// This is the CODE WE WRITE:
//
// enum Direction {
//     NORTH(0),
//     EAST(90),
//     SOUTH(180),
//     WEST(270);
//
//     private int degrees;
//
//     Direction(int degrees) {
//         this.degrees = degrees;
//     }
//
//     public int getDegrees() {
//         return degrees;
//     }
// }
//
// ============================================================
// IMPORTANT:
// The compiler generates enum machinery internally.
// The right side below is a CONCEPTUAL representation
// of what is happening internally.
// ============================================================

enum Direction {

    // --------------------------------------------------------
    // These are enum CONSTANTS.
    //
    // Each constant is actually an OBJECT.
    //
    // NORTH → Direction object with degrees = 0
    // EAST  → Direction object with degrees = 90
    // SOUTH → Direction object with degrees = 180
    // WEST  → Direction object with degrees = 270
    // --------------------------------------------------------

    NORTH(0),
    EAST(90),
    SOUTH(180),
    WEST(270);


    // --------------------------------------------------------
    // Every Direction object has its own degrees value.
    // --------------------------------------------------------

    private int degrees;


    // --------------------------------------------------------
    // Constructor
    //
    // This constructor is called automatically when the
    // enum constants are created.
    //
    // NORTH(0)
    //     ↓
    // Direction(0)
    //
    // EAST(90)
    //     ↓
    // Direction(90)
    // --------------------------------------------------------

    Direction(int degrees) {
        this.degrees = degrees;
    }


    // --------------------------------------------------------
    // Getter
    // --------------------------------------------------------

    public int getDegrees() {
        return degrees;
    }
}


// ============================================================
// CONCEPTUAL INTERNAL REPRESENTATION
// ============================================================
//
// The compiler creates something conceptually similar to:
//
// final class Direction extends Enum<Direction> {
//
//     public static final Direction NORTH =
//             new Direction(0);
//
//     public static final Direction EAST =
//             new Direction(90);
//
//     public static final Direction SOUTH =
//             new Direction(180);
//
//     public static final Direction WEST =
//             new Direction(270);
//
//
//     private int degrees;
//
//
//     private Direction(int degrees) {
//         this.degrees = degrees;
//     }
//
//
//     public int getDegrees() {
//         return degrees;
//     }
// }
//
// ============================================================
// IMPORTANT:
// You CANNOT actually write this class yourself as the enum's
// implementation. Java creates this structure for you.
// ============================================================


// ============================================================
// MAIN
// ============================================================

public class Main {

    public static void main(String[] args) {

        // d refers to the NORTH enum object.

        Direction d = Direction.NORTH;


        // getDegrees() is called on the NORTH object.

        System.out.println(d.getDegrees());

        // Output:
        // 0


        // EAST is a different Direction object.

        Direction d2 = Direction.EAST;

        System.out.println(d2.getDegrees());

        // Output:
        // 90


        // SOUTH

        Direction d3 = Direction.SOUTH;

        System.out.println(d3.getDegrees());

        // Output:
        // 180
    }
}
