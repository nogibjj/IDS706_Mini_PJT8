mod lib;
use csv::ReaderBuilder;
use std::error::Error;
use std::fs::File;
use std::process::Command;
use std::time::Instant;

fn main() -> Result<(), Box<dyn Error>> {
    let start_time = Instant::now();
    let file = File::open("heightweight.csv")?;

    let mut rdr = ReaderBuilder::new()
        .delimiter(b';') 
        .has_headers(true)
        .from_reader(file);

    let headers = rdr.headers()?;
    let weight_index = headers
        .iter()
        .position(|h| h == "Weight")
        .ok_or("Weight column not found")?;

    let mut weights: Vec<f64> = Vec::new();
    for result in rdr.records() {
        let record = result?;
        if let Some(weight_str) = record.get(weight_index) {
            if let Ok(weight) = weight_str.parse::<f64>() {
                weights.push(weight);
            }
        }
    }

    let stats = lib::compute_statistics(&weights);
    println!("Mean: {}", stats.mean);
    println!("Median: {}", stats.median);
    println!("Standard Deviation: {}", stats.std);
    println!("Size: {}", stats.size);
    let end_time = Instant::now();

    let elapsed_time = end_time.duration_since(start_time);
    println!("Total execution time: {:?}", elapsed_time); 
                                                         
    let mem_info = sys_info::mem_info().unwrap();
    println!(
        "Memory Usage: {}%",
        (mem_info.total - mem_info.avail) as f32 / mem_info.total as f32 * 100.0
    );

    let output = Command::new("ps")
        .arg("-o")
        .arg("%cpu")
        .arg("-p")
        .arg(format!("{}", std::process::id()))
        .output()
        .expect("Failed to execute ps command");

    let usage = String::from_utf8_lossy(&output.stdout);
    let lines: Vec<&str> = usage.split('\n').collect();

    if lines.len() >= 2 {
        let usage_str = lines[1].trim();
        let usage_float: Result<f32, _> = usage_str.parse();
        match usage_float {
            Ok(usage) => println!("CPU Usage: {:.2}%", usage),
            Err(_) => println!("Failed to parse CPU usage"),
        }
    } else {
        println!("Failed to get CPU usage");
    }
    Ok(())
}
