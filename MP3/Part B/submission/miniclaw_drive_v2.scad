// MiniClaw drive housing checkpoint 2
// Revised after skill-guided review with MiniClaw MCP context.

module_name = "MiniClaw drive housing v2";
housing_wall = 2.0;       // mm, ACME-VND-002 PLA recommendation
pinion_teeth = 14;        // module 1.0 minimum per ACME-ENG-001
output_teeth = 84;        // keeps 6:1 reduction after pinion change
gear_module = 1.0;
face_width = 5.0;         // mm, inside 4-6x module production range
nominal_backlash = 0.12;  // mm, ACME-ENG-001 PLA range
pivot_bore = 3.20;        // clearance fit; retained pin instead of press fit
root_fillet = 0.6;        // mm, reduces tooth-root stress concentration

module gear_disc(teeth, radius, width) {
  cylinder(h = width, r = radius, $fn = teeth * 2);
}

difference() {
  cube([90, 46, 9], center = true);
  translate([0, 0, -1]) cube([90 - 2 * housing_wall, 46 - 2 * housing_wall, 11], center = true);
  translate([-26, 0, -5]) cylinder(h = 14, d = pivot_bore, $fn = 48);
  translate([26, 0, -5]) cylinder(h = 14, d = pivot_bore, $fn = 48);
}

translate([-26, 0, 5.5]) gear_disc(pinion_teeth, pinion_teeth * gear_module / 2, face_width);
translate([26, 0, 5.5]) gear_disc(output_teeth, output_teeth * gear_module / 2, face_width);
