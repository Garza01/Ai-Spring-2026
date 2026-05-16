// MiniClaw drive housing checkpoint 1
// OpenSCAD concept source used for MP3 Part B CAD review.

module_name = "MiniClaw drive housing v1";
housing_wall = 1.0;       // mm, copied too closely from BigClaw aluminum
pinion_teeth = 12;        // module 1.0, below ACME-ENG-001 minimum
output_teeth = 72;
gear_module = 1.0;
face_width = 4.0;         // mm
nominal_backlash = 0.08;  // mm, too tight for PLA
pivot_bore = 3.02;        // mm for 3.00 mm pin

// Visual placeholder geometry. The review focused on parameters above.
module gear_disc(teeth, radius, width) {
  cylinder(h = width, r = radius, $fn = teeth * 2);
}

difference() {
  cube([86, 42, 8], center = true);
  translate([0, 0, -1]) cube([86 - 2 * housing_wall, 42 - 2 * housing_wall, 10], center = true);
  translate([-24, 0, -5]) cylinder(h = 12, d = pivot_bore, $fn = 48);
  translate([24, 0, -5]) cylinder(h = 12, d = pivot_bore, $fn = 48);
}

translate([-24, 0, 5]) gear_disc(pinion_teeth, pinion_teeth * gear_module / 2, face_width);
translate([24, 0, 5]) gear_disc(output_teeth, output_teeth * gear_module / 2, face_width);
