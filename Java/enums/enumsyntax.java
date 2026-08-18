// ============================================================
//                         ENUM
// ============================================================
//
// An enum is a special type in Java used to represent a
// FIXED SET of constants.
//
// Example:
//
//     enum Direction {
//         NORTH,
//         SOUTH,
//         EAST,
//         WEST
//     }
//
// ============================================================
// IMPORTANT:
// ============================================================
//
// We CANNOT actually write:
//
//     class Direction extends Enum<Direction>
//
// ourselves.
//
// Java automatically makes an enum extend:
//
//     Enum<Direction>
//
// Conceptually, Java creates something similar internally:
//
//     final class Direction extends Enum<Direction>
//
// ============================================================
public class enumsyntax {
    // --------------------------------------------------------
    // Creating an enum
    // --------------------------------------------------------
    //
    // Java internally creates objects for:
    //
    //     NORTH
    //     SOUTH
    //     EAST
    //     WEST
    //
    // Conceptually:
    //
    //     public static final Direction NORTH = new Direction(...);
    //     public static final Direction SOUTH = new Direction(...);
    //     public static final Direction EAST  = new Direction(...);
    //     public static final Direction WEST  = new Direction(...);
    //
    // The constructor is private internally, so we cannot
    // create another Direction object using new.
    //
    //     new Direction();     // ❌
    //
    // --------------------------------------------------------

    enum Direction {

        NORTH,
        SOUTH,
        EAST,
        WEST
    }


    public static void main(String[] args) {

        // ----------------------------------------------------
        // d1 stores the reference to the NORTH enum object.
        // ----------------------------------------------------

        Direction d1 = Direction.NORTH;


        // ----------------------------------------------------
        // d2 stores the reference to the SOUTH enum object.
        // ----------------------------------------------------

        Direction d2 = Direction.SOUTH;


        // ----------------------------------------------------
        // d3 also stores the reference to the NORTH enum object.
        //
        // IMPORTANT:
        // d1 and d3 point to the SAME NORTH object.
        // ----------------------------------------------------

        Direction d3 = Direction.NORTH;


        // ----------------------------------------------------
        // Printing enum objects
        // ----------------------------------------------------

        System.out.println(d1);   // NORTH
        System.out.println(d2);   // SOUTH
        System.out.println(d3);   // NORTH


        // ----------------------------------------------------
        // d1 and d3 point to the same enum constant.
        //
        // Therefore == returns true.
        // ----------------------------------------------------

        System.out.println(d1 == d3);   // true


        // ----------------------------------------------------
        // d1 points to NORTH.
        // d2 points to SOUTH.
        //
        // They are different enum objects.
        // ----------------------------------------------------

        System.out.println(d1 == d2);   // false


        // ----------------------------------------------------
        // instanceof
        //
        // Every enum is a subclass of java.lang.Enum.
        // Therefore d1 is an instance of Enum.
        // ----------------------------------------------------

        System.out.println(d1 instanceof Enum);   // true


        // ----------------------------------------------------
        // getClass()
        //
        // Gives the actual runtime class of d1.
        // ----------------------------------------------------

        System.out.println(d1.getClass());


        // ----------------------------------------------------
        // name()
        //
        // Returns the name of the enum constant.
        // ----------------------------------------------------

        System.out.println(d1.name());   // NORTH


        // ----------------------------------------------------
        // ordinal()
        //
        // Gives the position of the enum constant.
        //
        // Position starts from 0.
        //
        // NORTH → 0
        // SOUTH → 1
        // EAST  → 2
        // WEST  → 3
        // ----------------------------------------------------

        System.out.println(d1.ordinal());   // 0
        System.out.println(d2.ordinal());   // 1
    }
}


// ============================================================
//                         OUTPUT
// ============================================================
//
// NORTH
// SOUTH
// NORTH
// true
// false
// true
// class EnumExample$Direction
// NORTH
// 0
// 1
//
// ============================================================
//                  INTERNAL IDEA
// ============================================================
//
// Conceptually, the enum looks like:
//
//     final class Direction extends Enum<Direction> {
//
//         public static final Direction NORTH = ...;
//         public static final Direction SOUTH = ...;
//         public static final Direction EAST  = ...;
//         public static final Direction WEST  = ...;
//
//         private Direction(...) {
//         }
//     }
//
// ============================================================
//
// So:
//
//     Direction d1 = Direction.NORTH;
//
// means:
//
//     d1 ───────────────► NORTH object
//
// And:
//
//     Direction d3 = Direction.NORTH;
//
// means:
//
//     d3 ───────────────► SAME NORTH object
//
// Therefore:
//
//     d1 == d3
//
// gives:
//
//     true
//
// ============================================================
//
// MAIN IDEA:
//
// enum
//   ↓
// special class
//   ↓
// automatically extends Enum
//   ↓
// contains fixed predefined objects
//   ↓
// NORTH, SOUTH, EAST, WEST
//
// ============================================================
