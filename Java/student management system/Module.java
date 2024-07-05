/**
 status – corresponds to the assessment pattern for the module: 0 – coursework
 only, 1 – exam only, 2 – coursework and exam.
 */
enum ModuleStatus{
    CW_ONLY,
    EXAM_ONLY,
    CW_AND_EXAM
}

/**
 * Base class for all modules
 */
public abstract class Module {
    private String name;
    private ModuleStatus status;
    private double finalMark;

    // Constructor
    public Module(String name, ModuleStatus status) {
        this.name = name;
        this.status = status;
    }

    /**
     * Getter and setter methods for name attribute
     */
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Getter and setter methods for status attribute
     */

    public ModuleStatus getStatus() {
        return status;
    }
    public void setStatus(ModuleStatus status) {
        this.status = status;
    }

    // Getter and setter methods for finalMark attribute
    public double getFinalMark() {
        return finalMark;
    }
    public void setFinalMark(double finalMark) {
        this.finalMark = finalMark;
    }

    /**
     * Method to print final mark
     */

    public void printFinalMark() {
        System.out.println("Final mark for " + name + " is " + finalMark);
    }

    public abstract String getHeader();
    public abstract String getMarks();

}
