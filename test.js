// Setup
function phoneticLookup(val) {
    let result = "";
  
    // Only change code below this line
    const loookup = {
      'alpha': 'Adams',
      'brave': 'Boston',
      'charlie': 'Chicago',
      'delta': 'Denver',
      'echo': 'Easy',
      'Foxtrot': 'Frank'
    };
    result = lookup[val];
  
    // Only change code above this line
    return result;
  }
  
  phoneticLookup("charlie");